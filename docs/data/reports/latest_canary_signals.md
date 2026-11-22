# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T13:52:30.158420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `13`; crypto_alt avg `-0.0267` n `239`; crypto_major avg `-0.2127` n `8`; equity avg `-0.1278` n `166`; fx avg `-0.0058` n `6`; index avg `-0.0049` n `27`; metal avg `-0.0116` n `20`; unknown avg `0.424` n `1263`
- 1h: commodity avg `-0.0178` n `13`; crypto_alt avg `-0.0945` n `239`; crypto_major avg `-0.2036` n `8`; equity avg `-0.0156` n `166`; fx avg `-0.0013` n `6`; index avg `0.0369` n `27`; metal avg `-0.0223` n `20`; unknown avg `0.4754` n `1259`
- 4h: commodity avg `-0.0328` n `13`; crypto_alt avg `0.3123` n `239`; crypto_major avg `-0.174` n `8`; equity avg `0.2257` n `166`; fx avg `-0.0045` n `6`; index avg `0.0747` n `27`; metal avg `-0.0064` n `20`; unknown avg `84.1305` n `1197`
- 24h: commodity avg `-0.0268` n `13`; crypto_alt avg `0.574` n `239`; crypto_major avg `0.1281` n `8`; equity avg `0.687` n `166`; fx avg `-0.0055` n `6`; index avg `0.1351` n `27`; metal avg `-0.0412` n `20`; unknown avg `0.362` n `1084`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
