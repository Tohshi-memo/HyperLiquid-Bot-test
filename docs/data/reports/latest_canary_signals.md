# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T09:22:57.692465+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `12`; crypto_alt avg `-0.2734` n `230`; crypto_major avg `-0.34` n `8`; equity avg `-0.0451` n `92`; fx avg `0.0002` n `6`; index avg `-0.0102` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.9152` n `765`
- 1h: commodity avg `0.071` n `12`; crypto_alt avg `-0.3467` n `230`; crypto_major avg `-0.3672` n `8`; equity avg `0.0019` n `92`; fx avg `-0.0028` n `6`; index avg `0.002` n `25`; metal avg `-0.0032` n `20`; unknown avg `4.2087` n `765`
- 4h: commodity avg `0.0853` n `12`; crypto_alt avg `-0.4423` n `230`; crypto_major avg `-0.2696` n `8`; equity avg `-0.1` n `92`; fx avg `0.0028` n `6`; index avg `-0.0068` n `25`; metal avg `-0.026` n `20`; unknown avg `2.0044` n `747`
- 24h: commodity avg `0.5018` n `12`; crypto_alt avg `-1.0499` n `230`; crypto_major avg `-0.9792` n `8`; equity avg `-0.1818` n `92`; fx avg `0.0026` n `6`; index avg `-0.116` n `25`; metal avg `-0.1156` n `20`; unknown avg `0.0019` n `747`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
