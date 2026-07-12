# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T06:52:30.088114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.0023` n `230`; crypto_major avg `-0.0302` n `8`; equity avg `0.0007` n `92`; fx avg `-0.006` n `6`; index avg `-0.001` n `25`; metal avg `-0.0002` n `20`; unknown avg `-0.023` n `765`
- 1h: commodity avg `0.0067` n `12`; crypto_alt avg `-0.3782` n `230`; crypto_major avg `-0.3511` n `8`; equity avg `-0.1082` n `92`; fx avg `-0.0126` n `6`; index avg `-0.0239` n `25`; metal avg `-0.0087` n `20`; unknown avg `-0.2328` n `749`
- 4h: commodity avg `-0.0072` n `12`; crypto_alt avg `-0.3846` n `230`; crypto_major avg `-0.5297` n `8`; equity avg `-0.1463` n `92`; fx avg `-0.0098` n `6`; index avg `-0.0251` n `25`; metal avg `-0.0119` n `20`; unknown avg `-0.2851` n `749`
- 24h: commodity avg `0.4221` n `12`; crypto_alt avg `-0.8573` n `230`; crypto_major avg `-0.9074` n `8`; equity avg `-0.1957` n `92`; fx avg `-0.0102` n `6`; index avg `-0.1186` n `25`; metal avg `-0.1054` n `20`; unknown avg `-0.1097` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1758`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
