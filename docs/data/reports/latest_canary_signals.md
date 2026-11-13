# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T18:52:27.364146+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0144` n `13`; crypto_alt avg `0.0307` n `239`; crypto_major avg `0.0179` n `8`; equity avg `0.0707` n `162`; fx avg `-0.0011` n `6`; index avg `0.0184` n `27`; metal avg `-0.0179` n `20`; unknown avg `5.8283` n `1262`
- 1h: commodity avg `0.1051` n `13`; crypto_alt avg `0.0341` n `239`; crypto_major avg `0.0469` n `8`; equity avg `0.28` n `162`; fx avg `-0.0268` n `6`; index avg `0.0339` n `27`; metal avg `-0.0604` n `20`; unknown avg `-0.156` n `1260`
- 4h: commodity avg `-0.2318` n `13`; crypto_alt avg `-0.5543` n `239`; crypto_major avg `-0.6493` n `8`; equity avg `-0.3331` n `162`; fx avg `-0.0924` n `6`; index avg `-0.053` n `27`; metal avg `-0.2688` n `20`; unknown avg `-0.5416` n `1250`
- 24h: commodity avg `-0.1057` n `13`; crypto_alt avg `0.3751` n `239`; crypto_major avg `-1.2092` n `8`; equity avg `-2.4642` n `162`; fx avg `-0.0587` n `6`; index avg `-0.1954` n `27`; metal avg `-0.2354` n `20`; unknown avg `0.5958` n `1089`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
