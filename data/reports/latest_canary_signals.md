# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T12:52:27.774003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0671` n `12`; crypto_alt avg `-0.0619` n `230`; crypto_major avg `-0.0044` n `8`; equity avg `0.0362` n `113`; fx avg `-0.0003` n `6`; index avg `0.0168` n `25`; metal avg `0.0357` n `20`; unknown avg `0.0828` n `787`
- 1h: commodity avg `-0.0168` n `12`; crypto_alt avg `0.1924` n `230`; crypto_major avg `0.3129` n `8`; equity avg `-0.0759` n `113`; fx avg `-0.0124` n `6`; index avg `0.0092` n `25`; metal avg `0.0514` n `20`; unknown avg `0.0839` n `787`
- 4h: commodity avg `-0.0973` n `12`; crypto_alt avg `0.0281` n `230`; crypto_major avg `-0.1471` n `8`; equity avg `0.101` n `113`; fx avg `-0.0157` n `6`; index avg `0.0425` n `25`; metal avg `0.1661` n `20`; unknown avg `0.0294` n `787`
- 24h: commodity avg `-0.4253` n `12`; crypto_alt avg `-0.8743` n `230`; crypto_major avg `-0.3652` n `8`; equity avg `0.5635` n `113`; fx avg `-0.0065` n `6`; index avg `0.0738` n `25`; metal avg `-0.5106` n `20`; unknown avg `0.3729` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2265`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
