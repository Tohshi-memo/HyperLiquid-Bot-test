# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T04:37:32.369241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `-0.2164` n `230`; crypto_major avg `-0.222` n `8`; equity avg `-0.0404` n `92`; fx avg `-0.0036` n `6`; index avg `-0.0066` n `25`; metal avg `0.0002` n `20`; unknown avg `0.5434` n `765`
- 1h: commodity avg `0.0345` n `12`; crypto_alt avg `-0.198` n `230`; crypto_major avg `-0.2352` n `8`; equity avg `-0.0426` n `92`; fx avg `-0.0054` n `6`; index avg `0.0294` n `25`; metal avg `-0.002` n `20`; unknown avg `-0.3411` n `765`
- 4h: commodity avg `-0.1492` n `12`; crypto_alt avg `0.8462` n `230`; crypto_major avg `0.4892` n `8`; equity avg `0.0309` n `92`; fx avg `-0.0068` n `6`; index avg `-0.013` n `25`; metal avg `-0.002` n `20`; unknown avg `-0.0848` n `765`
- 24h: commodity avg `0.4546` n `12`; crypto_alt avg `-0.5663` n `229`; crypto_major avg `-0.5376` n `8`; equity avg `0.0885` n `92`; fx avg `0.016` n `6`; index avg `-0.0975` n `25`; metal avg `-0.0972` n `20`; unknown avg `-0.0561` n `729`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
