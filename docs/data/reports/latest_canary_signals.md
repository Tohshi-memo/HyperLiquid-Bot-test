# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T20:22:24.085141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `13`; crypto_alt avg `0.0148` n `239`; crypto_major avg `-0.1281` n `8`; equity avg `-0.0056` n `166`; fx avg `0.0034` n `6`; index avg `0.0129` n `27`; metal avg `-0.0011` n `20`; unknown avg `-0.1237` n `1258`
- 1h: commodity avg `0.0028` n `13`; crypto_alt avg `-0.0862` n `239`; crypto_major avg `-0.1962` n `8`; equity avg `0.0114` n `166`; fx avg `0.0054` n `6`; index avg `-0.0021` n `27`; metal avg `0.0009` n `20`; unknown avg `1.7846` n `1244`
- 4h: commodity avg `-0.0248` n `13`; crypto_alt avg `-0.6199` n `239`; crypto_major avg `-0.7264` n `8`; equity avg `0.0522` n `166`; fx avg `0.009` n `6`; index avg `-0.006` n `27`; metal avg `-0.059` n `20`; unknown avg `162.6662` n `1231`
- 24h: commodity avg `-0.1258` n `13`; crypto_alt avg `0.6211` n `239`; crypto_major avg `0.2517` n `8`; equity avg `0.8575` n `166`; fx avg `-0.0051` n `6`; index avg `0.1099` n `27`; metal avg `-0.0262` n `20`; unknown avg `189.2815` n `1052`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
