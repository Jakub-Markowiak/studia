###
# Jakub Markowiak
# nr indeksu: 255705
# 07.07.2021
###

bootstrap_interval <- function(x, B = 1000, alpha = 0.05) {
  M <- matrix(runif(B), nrow = B, ncol = 1) # macierz B x 1
  fill <- function(v) { # funkcja pomocnicza tworząca kolejne replikacje
    return (sample(x, replace = TRUE))
  }
  M <- t(sapply(M, fill)) # wypełnienie macierzy kolejnymi replikacjami x (1 wiersz - 1 replikacja)
  find_medians <- function(v) { # funkcja pomocnicza do utworzenia wektora median m
    return (median(M[v, ]))
  }
  m <- sapply(c(1:B), find_medians) # wektor median kolejnych replikacji
  boundries <- quantile(m, prob = c(alpha/2, 1 - alpha/2)) # kwantyle próbkowe z wektora m
  TL <- as.numeric(boundries[1])
  TU <- as.numeric(boundries[2])
  interval <- data.frame(lower = TL, upper = TU) # przedział ufności na poziomie istotności alpha
  return(interval)
}


###
# Testy
###

# normalny
x <- rnorm(1000, mean = 5)
(Boot <- bootstrap_interval(x, B = 1000, alpha = 0.01))
Boot$lower
Boot$upper

# jednostajny 
x <- runif(1000) * 10
bootstrap_interval(x, B = 1000, alpha = 0.02)

# dwumianowy
x <- rbinom(10, 100, 0.5)
bootstrap_interval(x, B = 250, alpha = 0.01)

# Poissona
x <- rpois(100, 10)
bootstrap_interval(x, B = 100, alpha = 0.1)

# wykładniczy
x <- rexp(10, 2)
bootstrap_interval(x, B = 1000, alpha = 0.5)

