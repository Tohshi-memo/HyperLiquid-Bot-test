# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T07:30:21.537844+00:00`
- Correlation status: `ready`
- Asset price records: `53`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `7`; crypto_alt avg `0.0611` n `223`; crypto_major avg `0.0215` n `7`; equity avg `0.0114` n `42`; fx avg `-0.0229` n `4`; index avg `-0.01` n `9`; metal avg `0.0` n `7`; unknown avg `-0.0373` n `311`
- 1h: commodity avg `-0.0287` n `7`; crypto_alt avg `0.3116` n `223`; crypto_major avg `0.2893` n `7`; equity avg `0.1418` n `42`; fx avg `-0.0216` n `4`; index avg `-0.0228` n `9`; metal avg `0.0181` n `7`; unknown avg `0.0975` n `311`
- 4h: commodity avg `-0.0267` n `7`; crypto_alt avg `-0.0711` n `223`; crypto_major avg `-0.0202` n `7`; equity avg `0.2024` n `42`; fx avg `-0.1381` n `4`; index avg `-0.0423` n `9`; metal avg `0.0172` n `7`; unknown avg `-0.1368` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.609`, n `49`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5877`, n `49`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5828`, n `45`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5677`, n `49`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5429`, n `45`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5349`, n `49`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4932`, n `49`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4611`, n `45`, moderate_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.4551`, n `45`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4449`, n `45`, moderate_sample_signal
