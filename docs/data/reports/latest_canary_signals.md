# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T18:52:33.190601+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `0.1443` n `230`; crypto_major avg `0.2939` n `8`; equity avg `0.1006` n `102`; fx avg `0.0102` n `6`; index avg `0.0173` n `25`; metal avg `-0.0035` n `20`; unknown avg `0.0197` n `780`
- 1h: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.2545` n `230`; crypto_major avg `-0.1861` n `8`; equity avg `-0.0599` n `102`; fx avg `0.0796` n `6`; index avg `0.0091` n `25`; metal avg `0.0274` n `20`; unknown avg `7.3478` n `780`
- 4h: commodity avg `-0.1363` n `12`; crypto_alt avg `0.3525` n `230`; crypto_major avg `0.025` n `8`; equity avg `0.2689` n `102`; fx avg `0.0847` n `6`; index avg `0.0896` n `25`; metal avg `0.1236` n `20`; unknown avg `10.6634` n `780`
- 24h: commodity avg `0.2142` n `12`; crypto_alt avg `-0.1729` n `230`; crypto_major avg `-1.6323` n `8`; equity avg `0.9201` n `102`; fx avg `0.2485` n `6`; index avg `0.3412` n `25`; metal avg `-0.2287` n `20`; unknown avg `0.3593` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
