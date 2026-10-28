# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T10:52:29.753019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.44` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.08` n `13`; crypto_alt avg `0.0385` n `238`; crypto_major avg `0.0509` n `8`; equity avg `0.0949` n `154`; fx avg `-0.0176` n `6`; index avg `0.0072` n `27`; metal avg `0.0133` n `20`; unknown avg `-0.0995` n `1239`
- 1h: commodity avg `0.1216` n `13`; crypto_alt avg `-0.0296` n `238`; crypto_major avg `0.0702` n `8`; equity avg `0.3904` n `154`; fx avg `-0.0165` n `6`; index avg `0.0345` n `27`; metal avg `-0.0307` n `20`; unknown avg `0.1972` n `1235`
- 4h: commodity avg `0.0053` n `13`; crypto_alt avg `0.5851` n `238`; crypto_major avg `0.8728` n `8`; equity avg `0.3547` n `154`; fx avg `0.0093` n `6`; index avg `0.0364` n `27`; metal avg `0.0159` n `20`; unknown avg `78.3592` n `1186`
- 24h: commodity avg `0.1302` n `13`; crypto_alt avg `2.3685` n `238`; crypto_major avg `2.6494` n `8`; equity avg `3.5024` n `154`; fx avg `0.0815` n `6`; index avg `0.4491` n `27`; metal avg `0.2517` n `20`; unknown avg `7.1081` n `1024`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1761`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
