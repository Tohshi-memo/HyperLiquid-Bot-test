# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T19:23:24.159102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.05` n `13`; crypto_alt avg `-0.0453` n `239`; crypto_major avg `-0.1141` n `8`; equity avg `-0.2748` n `161`; fx avg `0.0058` n `6`; index avg `-0.022` n `27`; metal avg `-0.0222` n `20`; unknown avg `20.9899` n `1260`
- 1h: commodity avg `-0.0329` n `13`; crypto_alt avg `-0.5904` n `239`; crypto_major avg `-0.6416` n `8`; equity avg `-0.7769` n `161`; fx avg `0.0096` n `6`; index avg `-0.0367` n `27`; metal avg `-0.0869` n `20`; unknown avg `21.0139` n `1256`
- 4h: commodity avg `-0.4589` n `13`; crypto_alt avg `-0.2115` n `239`; crypto_major avg `0.5775` n `8`; equity avg `0.7862` n `161`; fx avg `0.0148` n `6`; index avg `0.1398` n `27`; metal avg `-0.2753` n `20`; unknown avg `1.2025` n `1243`
- 24h: commodity avg `0.3784` n `13`; crypto_alt avg `0.8591` n `239`; crypto_major avg `1.2364` n `8`; equity avg `5.7463` n `161`; fx avg `-0.1451` n `6`; index avg `0.5684` n `27`; metal avg `-0.0047` n `20`; unknown avg `6.7806` n `1153`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
