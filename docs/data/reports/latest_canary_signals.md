# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T22:37:25.528288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `12`; crypto_alt avg `0.3632` n `234`; crypto_major avg `0.3686` n `8`; equity avg `0.0108` n `140`; fx avg `-0.0041` n `6`; index avg `0.001` n `26`; metal avg `-0.0038` n `20`; unknown avg `1.6499` n `943`
- 1h: commodity avg `-0.0205` n `12`; crypto_alt avg `0.4536` n `234`; crypto_major avg `0.2117` n `8`; equity avg `0.0237` n `140`; fx avg `0.0052` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0011` n `20`; unknown avg `1.1592` n `933`
- 4h: commodity avg `0.0288` n `12`; crypto_alt avg `-0.6809` n `234`; crypto_major avg `-0.9171` n `8`; equity avg `0.0793` n `140`; fx avg `-0.0338` n `6`; index avg `0.0107` n `26`; metal avg `-0.0031` n `20`; unknown avg `54.9845` n `911`
- 24h: commodity avg `0.0813` n `12`; crypto_alt avg `0.788` n `234`; crypto_major avg `-0.4071` n `8`; equity avg `-0.0051` n `140`; fx avg `-0.0593` n `6`; index avg `0.024` n `26`; metal avg `-0.0188` n `20`; unknown avg `6.271` n `838`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
