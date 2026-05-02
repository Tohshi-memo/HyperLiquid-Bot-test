# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T03:48:52.631814+00:00`
- Correlation status: `ready`
- Asset price records: `38`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `7`; crypto_alt avg `-0.1008` n `223`; crypto_major avg `-0.0382` n `7`; equity avg `0.0992` n `42`; fx avg `-0.0037` n `4`; index avg `0.0091` n `9`; metal avg `-0.007` n `7`; unknown avg `-0.1481` n `311`
- 1h: commodity avg `-0.007` n `7`; crypto_alt avg `-0.1171` n `223`; crypto_major avg `-0.015` n `7`; equity avg `0.0323` n `42`; fx avg `-0.0072` n `4`; index avg `0.0135` n `9`; metal avg `-0.0031` n `7`; unknown avg `-0.1255` n `311`
- 4h: commodity avg `-0.0421` n `7`; crypto_alt avg `0.0853` n `223`; crypto_major avg `0.2334` n `7`; equity avg `0.1326` n `42`; fx avg `-0.0167` n `4`; index avg `0.0483` n `9`; metal avg `-0.0053` n `7`; unknown avg `-0.0534` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6573`, n `34`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6337`, n `34`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5656`, n `34`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5437`, n `30`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5377`, n `30`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5338`, n `34`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5159`, n `34`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4949`, n `30`, moderate_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.4894`, n `34`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4859`, n `30`, moderate_sample_signal
