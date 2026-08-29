# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T01:07:23.327387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.3` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0177` n `12`; crypto_alt avg `-0.1546` n `231`; crypto_major avg `-0.0947` n `8`; equity avg `0.0105` n `127`; fx avg `-0.0038` n `6`; index avg `0.0076` n `26`; metal avg `-0.0203` n `20`; unknown avg `-0.0798` n `793`
- 1h: commodity avg `0.042` n `12`; crypto_alt avg `-0.2984` n `231`; crypto_major avg `-0.401` n `8`; equity avg `0.0002` n `127`; fx avg `-0.0007` n `6`; index avg `-0.0076` n `26`; metal avg `-0.0333` n `20`; unknown avg `0.0472` n `793`
- 4h: commodity avg `0.0103` n `12`; crypto_alt avg `0.3591` n `231`; crypto_major avg `0.1893` n `8`; equity avg `0.0285` n `127`; fx avg `0.0065` n `6`; index avg `-0.0058` n `26`; metal avg `0.0109` n `20`; unknown avg `0.255` n `793`
- 24h: commodity avg `-0.0859` n `12`; crypto_alt avg `-3.4344` n `231`; crypto_major avg `-3.662` n `8`; equity avg `-2.1295` n `127`; fx avg `-0.1147` n `6`; index avg `-0.2274` n `26`; metal avg `-0.3309` n `20`; unknown avg `-0.5442` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
