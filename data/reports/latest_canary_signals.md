# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T22:21:18.670717+00:00`
- Correlation status: `ready`
- Asset price records: `112`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `7`; crypto_alt avg `-0.1891` n `223`; crypto_major avg `-0.2273` n `7`; equity avg `-0.0479` n `42`; fx avg `-0.0008` n `4`; index avg `-0.0039` n `9`; metal avg `-0.0018` n `7`; unknown avg `0.0309` n `313`
- 1h: commodity avg `-0.0213` n `7`; crypto_alt avg `-0.0273` n `223`; crypto_major avg `0.0653` n `7`; equity avg `0.0044` n `42`; fx avg `0.025` n `4`; index avg `-0.024` n `9`; metal avg `0.0028` n `7`; unknown avg `0.0153` n `313`
- 4h: commodity avg `-0.0344` n `7`; crypto_alt avg `0.6727` n `223`; crypto_major avg `0.2331` n `7`; equity avg `0.359` n `42`; fx avg `0.0433` n `4`; index avg `0.0158` n `9`; metal avg `-0.0061` n `7`; unknown avg `0.2726` n `313`
- 24h: commodity avg `-0.1762` n `7`; crypto_alt avg `1.6355` n `223`; crypto_major avg `0.2732` n `7`; equity avg `0.8348` n `42`; fx avg `0.0489` n `4`; index avg `-0.0503` n `9`; metal avg `0.0167` n `7`; unknown avg `0.2876` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5284`, n `104`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5088`, n `104`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4916`, n `108`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4745`, n `108`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4509`, n `104`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4212`, n `104`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4181`, n `104`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4176`, n `104`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4164`, n `104`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4031`, n `108`, moderate_sample_signal
