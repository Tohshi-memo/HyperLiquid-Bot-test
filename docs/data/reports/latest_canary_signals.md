# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T19:37:37.787335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0218` n `12`; crypto_alt avg `-0.0731` n `230`; crypto_major avg `-0.083` n `8`; equity avg `-0.0861` n `113`; fx avg `-0.0023` n `6`; index avg `-0.0143` n `25`; metal avg `-0.0512` n `20`; unknown avg `-0.0706` n `786`
- 1h: commodity avg `-0.0557` n `12`; crypto_alt avg `-0.4024` n `230`; crypto_major avg `-0.2497` n `8`; equity avg `-0.228` n `113`; fx avg `-0.0053` n `6`; index avg `-0.0269` n `25`; metal avg `-0.0334` n `20`; unknown avg `-0.1802` n `786`
- 4h: commodity avg `-0.0644` n `12`; crypto_alt avg `-0.3783` n `230`; crypto_major avg `-0.2878` n `8`; equity avg `0.3967` n `113`; fx avg `-0.0151` n `6`; index avg `0.034` n `25`; metal avg `-0.1214` n `20`; unknown avg `0.3561` n `786`
- 24h: commodity avg `-0.0044` n `12`; crypto_alt avg `-0.5556` n `230`; crypto_major avg `0.5185` n `8`; equity avg `3.5086` n `113`; fx avg `0.0203` n `6`; index avg `0.3998` n `25`; metal avg `0.1995` n `20`; unknown avg `0.0972` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2267`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2042`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1957`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
