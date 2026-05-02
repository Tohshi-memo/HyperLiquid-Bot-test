# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T09:45:30.653333+00:00`
- Correlation status: `ready`
- Asset price records: `62`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0075` n `7`; crypto_alt avg `0.1369` n `223`; crypto_major avg `0.0902` n `7`; equity avg `0.0122` n `42`; fx avg `-0.0274` n `4`; index avg `-0.0313` n `9`; metal avg `0.0023` n `7`; unknown avg `-0.0037` n `313`
- 1h: commodity avg `-0.0008` n `7`; crypto_alt avg `0.3839` n `223`; crypto_major avg `0.1015` n `7`; equity avg `-0.1688` n `42`; fx avg `-0.0245` n `4`; index avg `-0.0162` n `9`; metal avg `0.0178` n `7`; unknown avg `0.0895` n `313`
- 4h: commodity avg `0.0332` n `7`; crypto_alt avg `0.6722` n `223`; crypto_major avg `0.4433` n `7`; equity avg `0.0494` n `42`; fx avg `0.0307` n `4`; index avg `-0.033` n `9`; metal avg `0.0918` n `7`; unknown avg `0.2378` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5769`, n `58`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5666`, n `54`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5638`, n `54`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5568`, n `58`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4894`, n `54`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4772`, n `54`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4696`, n `58`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4639`, n `54`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4408`, n `58`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4362`, n `58`, moderate_sample_signal
