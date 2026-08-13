# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T05:37:31.063272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0269` n `12`; crypto_alt avg `0.0367` n `230`; crypto_major avg `0.0562` n `8`; equity avg `-0.0573` n `113`; fx avg `0.0045` n `6`; index avg `-0.0224` n `25`; metal avg `-0.0144` n `20`; unknown avg `3.1021` n `787`
- 1h: commodity avg `0.0164` n `12`; crypto_alt avg `0.1461` n `230`; crypto_major avg `0.2655` n `8`; equity avg `0.1254` n `113`; fx avg `-0.0053` n `6`; index avg `-0.0023` n `25`; metal avg `0.0417` n `20`; unknown avg `2.5559` n `787`
- 4h: commodity avg `0.1217` n `12`; crypto_alt avg `0.4184` n `230`; crypto_major avg `0.7026` n `8`; equity avg `0.2867` n `113`; fx avg `0.0167` n `6`; index avg `0.0205` n `25`; metal avg `-0.1853` n `20`; unknown avg `2.8025` n `786`
- 24h: commodity avg `-0.1176` n `12`; crypto_alt avg `-0.8445` n `230`; crypto_major avg `0.2197` n `8`; equity avg `2.6152` n `113`; fx avg `-0.0387` n `6`; index avg `0.2921` n `25`; metal avg `-0.0738` n `20`; unknown avg `0.4016` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2441`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.212`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1648`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
