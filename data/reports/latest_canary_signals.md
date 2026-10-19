# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T19:37:30.370027+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0218` n `13`; crypto_alt avg `0.0588` n `237`; crypto_major avg `0.0704` n `8`; equity avg `0.2445` n `151`; fx avg `-0.005` n `6`; index avg `0.0217` n `26`; metal avg `0.0039` n `20`; unknown avg `10.2867` n `1196`
- 1h: commodity avg `-0.0067` n `13`; crypto_alt avg `0.3039` n `237`; crypto_major avg `0.1414` n `8`; equity avg `0.5881` n `151`; fx avg `0.0039` n `6`; index avg `0.075` n `26`; metal avg `-0.0014` n `20`; unknown avg `10.1581` n `1194`
- 4h: commodity avg `0.0783` n `13`; crypto_alt avg `-0.2272` n `237`; crypto_major avg `-0.2389` n `8`; equity avg `-0.7359` n `151`; fx avg `-0.0099` n `6`; index avg `-0.1225` n `26`; metal avg `-0.0301` n `20`; unknown avg `8.1563` n `1188`
- 24h: commodity avg `-0.2503` n `13`; crypto_alt avg `2.8441` n `237`; crypto_major avg `2.2384` n `8`; equity avg `3.3081` n `151`; fx avg `-0.0316` n `6`; index avg `0.6219` n `26`; metal avg `0.1277` n `20`; unknown avg `14.4154` n `920`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1945`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
