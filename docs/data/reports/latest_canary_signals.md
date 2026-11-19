# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T17:52:29.204107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0072` n `13`; crypto_alt avg `-0.3397` n `239`; crypto_major avg `-0.3796` n `8`; equity avg `-0.2587` n `165`; fx avg `0.0037` n `6`; index avg `-0.0189` n `27`; metal avg `-0.0589` n `20`; unknown avg `12.7714` n `1266`
- 1h: commodity avg `0.0037` n `13`; crypto_alt avg `0.111` n `239`; crypto_major avg `0.3937` n `8`; equity avg `-0.6482` n `165`; fx avg `-0.0015` n `6`; index avg `-0.0226` n `27`; metal avg `-0.0474` n `20`; unknown avg `2.1805` n `1264`
- 4h: commodity avg `-0.055` n `13`; crypto_alt avg `-1.673` n `239`; crypto_major avg `-1.2724` n `8`; equity avg `-2.4396` n `165`; fx avg `-0.0309` n `6`; index avg `-0.3285` n `27`; metal avg `-0.3487` n `20`; unknown avg `4.3586` n `1257`
- 24h: commodity avg `0.3739` n `13`; crypto_alt avg `-0.3635` n `239`; crypto_major avg `0.3437` n `8`; equity avg `-0.5544` n `165`; fx avg `0.0132` n `6`; index avg `0.0179` n `27`; metal avg `-0.3911` n `20`; unknown avg `4.4441` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
