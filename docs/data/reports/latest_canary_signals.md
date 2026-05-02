# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T06:45:21.641528+00:00`
- Correlation status: `ready`
- Asset price records: `50`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `7`; crypto_alt avg `0.0856` n `223`; crypto_major avg `0.1288` n `7`; equity avg `0.0751` n `42`; fx avg `-0.028` n `4`; index avg `-0.0009` n `9`; metal avg `0.0068` n `7`; unknown avg `0.1469` n `311`
- 1h: commodity avg `0.0064` n `7`; crypto_alt avg `0.0743` n `223`; crypto_major avg `0.0539` n `7`; equity avg `0.0838` n `42`; fx avg `-0.0104` n `4`; index avg `-0.0067` n `9`; metal avg `0.0366` n `7`; unknown avg `-0.0386` n `311`
- 4h: commodity avg `0.0012` n `7`; crypto_alt avg `-0.3135` n `223`; crypto_major avg `-0.1569` n `7`; equity avg `0.0634` n `42`; fx avg `-0.148` n `4`; index avg `-0.0161` n `9`; metal avg `0.0098` n `7`; unknown avg `-0.0698` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6479`, n `46`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6252`, n `46`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5763`, n `42`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5673`, n `46`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5554`, n `42`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5345`, n `46`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5026`, n `46`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4847`, n `42`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.482`, n `42`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4747`, n `42`, moderate_sample_signal
