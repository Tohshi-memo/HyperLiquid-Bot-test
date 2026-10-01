# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T08:52:32.369796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1108` n `13`; crypto_alt avg `0.2604` n `234`; crypto_major avg `0.1625` n `8`; equity avg `0.0989` n `142`; fx avg `-0.0156` n `6`; index avg `0.0162` n `26`; metal avg `-0.0306` n `20`; unknown avg `0.119` n `975`
- 1h: commodity avg `0.0237` n `13`; crypto_alt avg `0.0096` n `234`; crypto_major avg `0.0165` n `8`; equity avg `-0.2075` n `142`; fx avg `-0.0379` n `6`; index avg `-0.0369` n `26`; metal avg `-0.1508` n `20`; unknown avg `5.6431` n `957`
- 4h: commodity avg `0.7787` n `13`; crypto_alt avg `-1.0061` n `234`; crypto_major avg `-0.9692` n `8`; equity avg `-0.533` n `142`; fx avg `-0.0362` n `6`; index avg `-0.1561` n `26`; metal avg `-0.3815` n `20`; unknown avg `4.2398` n `930`
- 24h: commodity avg `0.0656` n `13`; crypto_alt avg `0.0344` n `234`; crypto_major avg `0.5404` n `8`; equity avg `0.158` n `142`; fx avg `0.0944` n `6`; index avg `0.0318` n `26`; metal avg `-0.4644` n `20`; unknown avg `774.2149` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
