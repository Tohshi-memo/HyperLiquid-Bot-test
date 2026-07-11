# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T08:52:26.212064+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `-0.0279` n `230`; crypto_major avg `-0.0534` n `8`; equity avg `-0.0318` n `92`; fx avg `0.0` n `6`; index avg `-0.0002` n `25`; metal avg `0.0005` n `20`; unknown avg `-0.0092` n `765`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `0.0536` n `230`; crypto_major avg `0.0801` n `8`; equity avg `-0.0088` n `92`; fx avg `-0.0008` n `6`; index avg `0.0019` n `25`; metal avg `0.0126` n `20`; unknown avg `-0.0039` n `765`
- 4h: commodity avg `0.0465` n `12`; crypto_alt avg `0.1025` n `230`; crypto_major avg `0.18` n `8`; equity avg `0.1143` n `92`; fx avg `0.0225` n `6`; index avg `0.0115` n `25`; metal avg `-0.012` n `20`; unknown avg `0.0184` n `733`
- 24h: commodity avg `-0.1981` n `12`; crypto_alt avg `0.1749` n `229`; crypto_major avg `-0.449` n `8`; equity avg `0.1192` n `92`; fx avg `-0.0617` n `6`; index avg `0.1888` n `25`; metal avg `0.2004` n `20`; unknown avg `2.8627` n `730`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
