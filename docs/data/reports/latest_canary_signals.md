# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T05:37:27.681217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0301` n `13`; crypto_alt avg `0.0172` n `238`; crypto_major avg `-0.0228` n `8`; equity avg `-0.0699` n `155`; fx avg `0.0021` n `6`; index avg `-0.0105` n `27`; metal avg `-0.0644` n `20`; unknown avg `4.0754` n `1238`
- 1h: commodity avg `-0.0638` n `13`; crypto_alt avg `0.8534` n `238`; crypto_major avg `0.6032` n `8`; equity avg `0.5293` n `155`; fx avg `-0.0045` n `6`; index avg `0.1359` n `27`; metal avg `0.0587` n `20`; unknown avg `0.5076` n `1226`
- 4h: commodity avg `-0.1767` n `13`; crypto_alt avg `-0.8224` n `238`; crypto_major avg `-0.29` n `8`; equity avg `0.1444` n `155`; fx avg `0.033` n `6`; index avg `0.1396` n `27`; metal avg `-0.1874` n `20`; unknown avg `1.2376` n `1196`
- 24h: commodity avg `-0.1904` n `13`; crypto_alt avg `-1.4824` n `238`; crypto_major avg `-0.825` n `8`; equity avg `-0.6746` n `154`; fx avg `0.0401` n `6`; index avg `0.053` n `27`; metal avg `-0.1691` n `20`; unknown avg `34.2579` n `974`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
