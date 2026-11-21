# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T18:07:24.625006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `13`; crypto_alt avg `0.0157` n `239`; crypto_major avg `0.1208` n `8`; equity avg `0.0703` n `166`; fx avg `0.0006` n `6`; index avg `-0.0639` n `27`; metal avg `0.0067` n `20`; unknown avg `-0.0405` n `1216`
- 1h: commodity avg `0.0183` n `13`; crypto_alt avg `0.1188` n `239`; crypto_major avg `0.1075` n `8`; equity avg `0.0069` n `166`; fx avg `-0.005` n `6`; index avg `-0.0726` n `27`; metal avg `0.0075` n `20`; unknown avg `0.6319` n `1210`
- 4h: commodity avg `0.0032` n `13`; crypto_alt avg `-0.1392` n `239`; crypto_major avg `-0.14` n `8`; equity avg `-0.0815` n `166`; fx avg `0.0014` n `6`; index avg `-0.1007` n `27`; metal avg `0.0016` n `20`; unknown avg `210.1544` n `1200`
- 24h: commodity avg `0.5019` n `13`; crypto_alt avg `0.9929` n `239`; crypto_major avg `1.7145` n `8`; equity avg `0.3097` n `166`; fx avg `-0.1117` n `6`; index avg `-0.0595` n `27`; metal avg `0.2104` n `20`; unknown avg `183.5376` n `1094`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
