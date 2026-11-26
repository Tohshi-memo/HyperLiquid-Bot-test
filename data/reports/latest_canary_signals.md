# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T03:22:37.253566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0338` n `13`; crypto_alt avg `0.0039` n `239`; crypto_major avg `0.0762` n `8`; equity avg `0.0339` n `168`; fx avg `0.0083` n `6`; index avg `-0.0039` n `27`; metal avg `-0.0489` n `20`; unknown avg `3.8689` n `1265`
- 1h: commodity avg `0.0599` n `13`; crypto_alt avg `-0.2673` n `239`; crypto_major avg `-0.2039` n `8`; equity avg `-0.2247` n `168`; fx avg `0.0266` n `6`; index avg `-0.0278` n `27`; metal avg `-0.0362` n `20`; unknown avg `4.2336` n `1263`
- 4h: commodity avg `0.0509` n `13`; crypto_alt avg `1.3237` n `239`; crypto_major avg `1.1146` n `8`; equity avg `1.2024` n `168`; fx avg `-0.0294` n `6`; index avg `0.1037` n `27`; metal avg `0.1531` n `20`; unknown avg `1.8937` n `1247`
- 24h: commodity avg `0.7057` n `13`; crypto_alt avg `3.618` n `239`; crypto_major avg `2.5821` n `8`; equity avg `2.1237` n `168`; fx avg `-0.0006` n `6`; index avg `0.1606` n `27`; metal avg `0.4428` n `20`; unknown avg `963.6881` n `1021`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1989`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
