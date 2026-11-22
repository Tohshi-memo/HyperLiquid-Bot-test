# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T12:37:35.268261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0` n `13`; crypto_alt avg `-0.2838` n `239`; crypto_major avg `-0.5477` n `8`; equity avg `-0.3091` n `166`; fx avg `0.0006` n `6`; index avg `-0.0277` n `27`; metal avg `-0.0591` n `20`; unknown avg `111.4278` n `1263`
- 1h: commodity avg `-0.0088` n `13`; crypto_alt avg `-0.3921` n `239`; crypto_major avg `-0.5969` n `8`; equity avg `-0.2667` n `166`; fx avg `0.0113` n `6`; index avg `-0.0302` n `27`; metal avg `-0.0254` n `20`; unknown avg `0.5737` n `1253`
- 4h: commodity avg `0.0018` n `13`; crypto_alt avg `0.2047` n `239`; crypto_major avg `0.1831` n `8`; equity avg `0.2724` n `166`; fx avg `-0.0192` n `6`; index avg `0.0074` n `27`; metal avg `0.0496` n `20`; unknown avg `138.3687` n `1149`
- 24h: commodity avg `0.0244` n `13`; crypto_alt avg `1.7752` n `239`; crypto_major avg `1.9136` n `8`; equity avg `1.4141` n `166`; fx avg `-0.0034` n `6`; index avg `0.1707` n `27`; metal avg `0.0898` n `20`; unknown avg `0.766` n `1084`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
