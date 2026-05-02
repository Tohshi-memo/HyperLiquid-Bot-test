# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T10:30:24.085234+00:00`
- Correlation status: `ready`
- Asset price records: `65`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `7`; crypto_alt avg `-0.0203` n `223`; crypto_major avg `-0.1031` n `7`; equity avg `0.0678` n `42`; fx avg `0.0` n `4`; index avg `0.0352` n `9`; metal avg `0.0015` n `7`; unknown avg `-0.0055` n `313`
- 1h: commodity avg `-0.0184` n `7`; crypto_alt avg `0.0377` n `223`; crypto_major avg `-0.0923` n `7`; equity avg `0.0777` n `42`; fx avg `-0.0197` n `4`; index avg `-0.0352` n `9`; metal avg `0.0112` n `7`; unknown avg `-0.0603` n `313`
- 4h: commodity avg `0.0212` n `7`; crypto_alt avg `0.5786` n `223`; crypto_major avg `0.3335` n `7`; equity avg `0.1077` n `42`; fx avg `0.0208` n `4`; index avg `-0.0312` n `9`; metal avg `0.0709` n `7`; unknown avg `0.3192` n `311`
- 24h: crypto_alt avg `0.8732` n `223`; crypto_major avg `0.6648` n `7`; metal avg `0.7928` n `1`; unknown avg `1.3794` n `310`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5772`, n `61`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5665`, n `57`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.566`, n `57`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5572`, n `61`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4921`, n `57`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4789`, n `61`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4766`, n `57`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4636`, n `57`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4446`, n `61`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4387`, n `61`, moderate_sample_signal
