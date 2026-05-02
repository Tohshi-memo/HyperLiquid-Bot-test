# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T15:45:24.202021+00:00`
- Correlation status: `ready`
- Asset price records: `86`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `7`; crypto_alt avg `0.0845` n `223`; crypto_major avg `0.0196` n `7`; equity avg `0.0175` n `42`; fx avg `0.0104` n `4`; index avg `0.0085` n `9`; metal avg `-0.006` n `7`; unknown avg `-0.0225` n `313`
- 1h: commodity avg `-0.014` n `7`; crypto_alt avg `0.3835` n `223`; crypto_major avg `0.0884` n `7`; equity avg `0.0325` n `42`; fx avg `0.0456` n `4`; index avg `0.0014` n `9`; metal avg `0.0086` n `7`; unknown avg `-0.1446` n `313`
- 4h: commodity avg `-0.0591` n `7`; crypto_alt avg `1.3696` n `223`; crypto_major avg `0.4832` n `7`; equity avg `-0.0112` n `42`; fx avg `0.0501` n `4`; index avg `0.0308` n `9`; metal avg `-0.0088` n `7`; unknown avg `0.0119` n `313`
- 24h: commodity avg `0.2775` n `7`; crypto_alt avg `1.2362` n `223`; crypto_major avg `-0.0846` n `7`; equity avg `0.5848` n `42`; fx avg `-0.1017` n `4`; index avg `0.0744` n `9`; metal avg `-0.3347` n `7`; unknown avg `0.8469` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5369`, n `78`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5325`, n `82`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5258`, n `78`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.514`, n `82`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4783`, n `78`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4776`, n `78`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4654`, n `78`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4584`, n `82`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4325`, n `82`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4263`, n `78`, moderate_sample_signal
