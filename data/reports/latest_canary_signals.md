# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T15:37:29.696098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3988` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7188` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0771` n `12`; crypto_alt avg `0.5656` n `228`; crypto_major avg `0.6828` n `8`; equity avg `0.5254` n `86`; fx avg `-0.0077` n `6`; index avg `0.1027` n `23`; metal avg `0.1084` n `20`; unknown avg `0.0009` n `765`
- 1h: commodity avg `-0.0906` n `12`; crypto_alt avg `1.184` n `228`; crypto_major avg `1.2611` n `8`; equity avg `0.5389` n `86`; fx avg `-0.0425` n `6`; index avg `0.1002` n `23`; metal avg `0.1487` n `20`; unknown avg `-0.0781` n `765`
- 4h: commodity avg `-0.2646` n `12`; crypto_alt avg `1.866` n `228`; crypto_major avg `2.1342` n `8`; equity avg `1.4962` n `86`; fx avg `-0.0395` n `6`; index avg `0.193` n `23`; metal avg `0.4154` n `20`; unknown avg `0.2246` n `765`
- 24h: commodity avg `-0.4659` n `12`; crypto_alt avg `2.2227` n `228`; crypto_major avg `2.9729` n `8`; equity avg `-0.2172` n `86`; fx avg `-0.0413` n `6`; index avg `-0.1651` n `23`; metal avg `0.6446` n `20`; unknown avg `0.0842` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2627`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
