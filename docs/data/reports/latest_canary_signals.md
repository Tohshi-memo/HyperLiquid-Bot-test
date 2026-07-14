# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T17:07:29.500745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0199` n `12`; crypto_alt avg `-0.1632` n `230`; crypto_major avg `-0.281` n `8`; equity avg `-0.0749` n `92`; fx avg `0.006` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0322` n `20`; unknown avg `0.1205` n `766`
- 1h: commodity avg `-0.0997` n `12`; crypto_alt avg `-0.1274` n `230`; crypto_major avg `-0.2992` n `8`; equity avg `0.1332` n `92`; fx avg `-0.0023` n `6`; index avg `0.0823` n `25`; metal avg `0.022` n `20`; unknown avg `-0.0227` n `766`
- 4h: commodity avg `-0.1564` n `12`; crypto_alt avg `0.5112` n `230`; crypto_major avg `0.706` n `8`; equity avg `-0.2717` n `92`; fx avg `-0.0128` n `6`; index avg `0.0738` n `25`; metal avg `-0.012` n `20`; unknown avg `-0.2115` n `758`
- 24h: commodity avg `0.6287` n `12`; crypto_alt avg `1.4575` n `230`; crypto_major avg `2.903` n `8`; equity avg `0.7787` n `92`; fx avg `-0.0298` n `6`; index avg `0.2919` n `25`; metal avg `0.5945` n `20`; unknown avg `-0.0952` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
