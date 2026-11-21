# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T22:52:30.805359+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0017` n `13`; crypto_alt avg `-0.0009` n `239`; crypto_major avg `-0.0694` n `8`; equity avg `-0.0043` n `166`; fx avg `0.0051` n `6`; index avg `-0.0009` n `27`; metal avg `0.0037` n `20`; unknown avg `0.1679` n `1254`
- 1h: commodity avg `-0.0053` n `13`; crypto_alt avg `-0.0955` n `239`; crypto_major avg `-0.3488` n `8`; equity avg `-0.0757` n `166`; fx avg `0.0037` n `6`; index avg `-0.0085` n `27`; metal avg `-0.0426` n `20`; unknown avg `214.8067` n `1246`
- 4h: commodity avg `0.0321` n `13`; crypto_alt avg `-0.2476` n `239`; crypto_major avg `-0.1847` n `8`; equity avg `0.1297` n `166`; fx avg `0.0108` n `6`; index avg `0.0398` n `27`; metal avg `-0.123` n `20`; unknown avg `47.0932` n `1196`
- 24h: commodity avg `0.0238` n `13`; crypto_alt avg `-0.1114` n `239`; crypto_major avg `1.4495` n `8`; equity avg `0.6101` n `166`; fx avg `-0.0314` n `6`; index avg `0.1575` n `27`; metal avg `0.1076` n `20`; unknown avg `238.4713` n `1080`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
