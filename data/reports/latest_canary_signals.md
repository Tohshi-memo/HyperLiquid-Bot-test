# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T04:52:33.270173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0268` n `12`; crypto_alt avg `-0.0465` n `230`; crypto_major avg `0.0087` n `8`; equity avg `0.024` n `92`; fx avg `0.0009` n `6`; index avg `0.0028` n `25`; metal avg `0.0006` n `20`; unknown avg `0.2591` n `765`
- 1h: commodity avg `0.0593` n `12`; crypto_alt avg `-0.2703` n `230`; crypto_major avg `-0.258` n `8`; equity avg `-0.0323` n `92`; fx avg `-0.0013` n `6`; index avg `0.0209` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.5991` n `765`
- 4h: commodity avg `-0.1154` n `12`; crypto_alt avg `0.8287` n `230`; crypto_major avg `0.4633` n `8`; equity avg `0.0715` n `92`; fx avg `-0.0006` n `6`; index avg `0.0031` n `25`; metal avg `0.0106` n `20`; unknown avg `0.0749` n `765`
- 24h: commodity avg `0.4705` n `12`; crypto_alt avg `-0.3533` n `230`; crypto_major avg `-0.3918` n `8`; equity avg `0.0927` n `92`; fx avg `0.0168` n `6`; index avg `-0.0931` n `25`; metal avg `-0.094` n `20`; unknown avg `0.0132` n `729`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1797`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
