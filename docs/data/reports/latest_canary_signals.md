# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T16:07:28.375702+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1367` n `13`; crypto_alt avg `-0.1206` n `237`; crypto_major avg `-0.127` n `8`; equity avg `-0.3873` n `151`; fx avg `-0.0089` n `6`; index avg `-0.0868` n `26`; metal avg `-0.0541` n `20`; unknown avg `0.0396` n `1188`
- 1h: commodity avg `0.2733` n `13`; crypto_alt avg `-0.1475` n `237`; crypto_major avg `-0.3205` n `8`; equity avg `0.026` n `151`; fx avg `-0.0208` n `6`; index avg `-0.001` n `26`; metal avg `-0.0238` n `20`; unknown avg `2.2877` n `1188`
- 4h: commodity avg `0.0674` n `13`; crypto_alt avg `-0.1807` n `237`; crypto_major avg `-0.636` n `8`; equity avg `-0.0686` n `151`; fx avg `-0.0213` n `6`; index avg `0.0715` n `26`; metal avg `-0.203` n `20`; unknown avg `-0.2005` n `1109`
- 24h: commodity avg `-0.1254` n `13`; crypto_alt avg `1.1448` n `237`; crypto_major avg `1.4513` n `8`; equity avg `3.3847` n `151`; fx avg `-0.0341` n `6`; index avg `0.6286` n `26`; metal avg `0.0751` n `20`; unknown avg `3.6589` n `916`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2198`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
