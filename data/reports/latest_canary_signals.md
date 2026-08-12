# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T17:07:32.039164+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.08` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0278` n `12`; crypto_alt avg `0.1776` n `230`; crypto_major avg `0.0807` n `8`; equity avg `0.0688` n `113`; fx avg `0.0032` n `6`; index avg `0.0162` n `25`; metal avg `0.0255` n `20`; unknown avg `0.3824` n `786`
- 1h: commodity avg `-0.051` n `12`; crypto_alt avg `0.0459` n `230`; crypto_major avg `0.0193` n `8`; equity avg `0.1312` n `113`; fx avg `-0.0048` n `6`; index avg `0.034` n `25`; metal avg `-0.1085` n `20`; unknown avg `0.3671` n `786`
- 4h: commodity avg `0.001` n `12`; crypto_alt avg `-0.5816` n `230`; crypto_major avg `-0.578` n `8`; equity avg `0.5527` n `113`; fx avg `0.0119` n `6`; index avg `-0.0111` n `25`; metal avg `-0.2561` n `20`; unknown avg `0.5853` n `786`
- 24h: commodity avg `0.0301` n `12`; crypto_alt avg `-0.0633` n `230`; crypto_major avg `1.0399` n `8`; equity avg `3.7203` n `113`; fx avg `0.0405` n `6`; index avg `0.4282` n `25`; metal avg `0.1454` n `20`; unknown avg `0.0468` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2277`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2021`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1963`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
