# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T06:07:31.371361+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `12`; crypto_alt avg `0.029` n `233`; crypto_major avg `-0.0721` n `8`; equity avg `-0.0628` n `136`; fx avg `0.0016` n `6`; index avg `-0.0092` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.0862` n `812`
- 1h: commodity avg `0.0568` n `12`; crypto_alt avg `0.1348` n `233`; crypto_major avg `0.0617` n `8`; equity avg `-0.1546` n `136`; fx avg `0.0014` n `6`; index avg `-0.0226` n `26`; metal avg `0.0019` n `20`; unknown avg `51.051` n `812`
- 4h: commodity avg `0.1057` n `12`; crypto_alt avg `0.1656` n `233`; crypto_major avg `-0.077` n `8`; equity avg `-0.2959` n `136`; fx avg `0.0044` n `6`; index avg `-0.0575` n `26`; metal avg `0.0044` n `20`; unknown avg `0.0154` n `786`
- 24h: commodity avg `0.1569` n `12`; crypto_alt avg `1.2966` n `233`; crypto_major avg `0.2359` n `8`; equity avg `-0.643` n `136`; fx avg `-0.0043` n `6`; index avg `-0.1` n `26`; metal avg `0.0419` n `20`; unknown avg `0.4266` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
