# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T18:52:27.405201+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0411` n `13`; crypto_alt avg `0.3025` n `237`; crypto_major avg `0.1938` n `8`; equity avg `0.1754` n `151`; fx avg `0.0014` n `6`; index avg `0.025` n `26`; metal avg `0.0326` n `20`; unknown avg `5.5898` n `1196`
- 1h: commodity avg `-0.3349` n `13`; crypto_alt avg `0.3163` n `237`; crypto_major avg `0.2145` n `8`; equity avg `0.0933` n `151`; fx avg `-0.0156` n `6`; index avg `0.0228` n `26`; metal avg `0.0375` n `20`; unknown avg `5.3951` n `1194`
- 4h: commodity avg `0.0868` n `13`; crypto_alt avg `-0.1344` n `237`; crypto_major avg `-0.314` n `8`; equity avg `-0.5884` n `151`; fx avg `0.0002` n `6`; index avg `-0.0396` n `26`; metal avg `0.0571` n `20`; unknown avg `6.7161` n `1187`
- 24h: commodity avg `-0.2797` n `13`; crypto_alt avg `1.4929` n `237`; crypto_major avg `1.4452` n `8`; equity avg `2.6757` n `151`; fx avg `-0.0366` n `6`; index avg `0.5642` n `26`; metal avg `0.1365` n `20`; unknown avg `9.5607` n `918`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1915`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
