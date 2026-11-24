# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T20:37:29.490162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `13`; crypto_alt avg `-0.2248` n `239`; crypto_major avg `-0.2936` n `8`; equity avg `-0.285` n `168`; fx avg `0.0011` n `6`; index avg `-0.0218` n `27`; metal avg `-0.0566` n `20`; unknown avg `0.1077` n `1265`
- 1h: commodity avg `-0.0821` n `13`; crypto_alt avg `-0.6199` n `239`; crypto_major avg `-0.4297` n `8`; equity avg `-0.5593` n `168`; fx avg `-0.0133` n `6`; index avg `-0.0751` n `27`; metal avg `-0.1191` n `20`; unknown avg `1.3311` n `1253`
- 4h: commodity avg `0.165` n `13`; crypto_alt avg `-0.1724` n `239`; crypto_major avg `0.0412` n `8`; equity avg `0.5168` n `168`; fx avg `-0.025` n `6`; index avg `0.0704` n `27`; metal avg `-0.0681` n `20`; unknown avg `170.5747` n `1225`
- 24h: commodity avg `0.5977` n `13`; crypto_alt avg `-3.5595` n `239`; crypto_major avg `-3.3123` n `8`; equity avg `-4.6554` n `167`; fx avg `0.2289` n `6`; index avg `-0.3433` n `27`; metal avg `-1.2067` n `20`; unknown avg `184.4548` n `1111`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
