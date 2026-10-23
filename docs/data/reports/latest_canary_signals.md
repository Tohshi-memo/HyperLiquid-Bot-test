# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T22:37:40.979564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `13`; crypto_alt avg `-0.8797` n `237`; crypto_major avg `-0.5689` n `8`; equity avg `-0.146` n `152`; fx avg `0.0067` n `6`; index avg `-0.0266` n `26`; metal avg `-0.0311` n `20`; unknown avg `1.5405` n `1230`
- 1h: commodity avg `0.0695` n `13`; crypto_alt avg `-0.9919` n `237`; crypto_major avg `-0.6097` n `8`; equity avg `-0.167` n `152`; fx avg `0.0475` n `6`; index avg `-0.0376` n `26`; metal avg `-0.0412` n `20`; unknown avg `0.8439` n `1220`
- 4h: commodity avg `0.2086` n `13`; crypto_alt avg `-1.9542` n `237`; crypto_major avg `-0.9292` n `8`; equity avg `-0.3847` n `152`; fx avg `0.0436` n `6`; index avg `-0.019` n `26`; metal avg `-0.0891` n `20`; unknown avg `-0.0911` n `1134`
- 24h: commodity avg `0.5241` n `13`; crypto_alt avg `-0.6889` n `237`; crypto_major avg `-0.2858` n `8`; equity avg `1.1582` n `152`; fx avg `-0.0085` n `6`; index avg `0.0537` n `26`; metal avg `-0.184` n `20`; unknown avg `199.4297` n `1024`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1996`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
