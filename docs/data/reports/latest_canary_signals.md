# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T01:52:34.699513+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `13`; crypto_alt avg `0.1614` n `239`; crypto_major avg `0.2048` n `8`; equity avg `0.0623` n `166`; fx avg `0.0` n `6`; index avg `0.0103` n `27`; metal avg `0.0113` n `20`; unknown avg `0.4623` n `1262`
- 1h: commodity avg `-0.0066` n `13`; crypto_alt avg `-0.2246` n `239`; crypto_major avg `-0.2024` n `8`; equity avg `-0.0199` n `166`; fx avg `0.0066` n `6`; index avg `0.0176` n `27`; metal avg `-0.0043` n `20`; unknown avg `1.213` n `1258`
- 4h: commodity avg `-0.0329` n `13`; crypto_alt avg `-0.1573` n `239`; crypto_major avg `-0.1615` n `8`; equity avg `0.4038` n `166`; fx avg `-0.0212` n `6`; index avg `0.0654` n `27`; metal avg `0.0296` n `20`; unknown avg `325.9589` n `1228`
- 24h: commodity avg `0.2813` n `13`; crypto_alt avg `-4.4383` n `239`; crypto_major avg `-5.2245` n `8`; equity avg `-4.8302` n `166`; fx avg `0.0075` n `6`; index avg `-0.5293` n `27`; metal avg `-0.1448` n `20`; unknown avg `12.6913` n `1121`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
