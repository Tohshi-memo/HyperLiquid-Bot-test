# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T21:07:26.908824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0181` n `13`; crypto_alt avg `-0.1683` n `237`; crypto_major avg `-0.092` n `8`; equity avg `0.0466` n `154`; fx avg `0.0011` n `6`; index avg `0.0086` n `27`; metal avg `0.0118` n `20`; unknown avg `131.4122` n `1228`
- 1h: commodity avg `-0.069` n `13`; crypto_alt avg `-0.2652` n `237`; crypto_major avg `-0.3448` n `8`; equity avg `0.1872` n `154`; fx avg `-0.0124` n `6`; index avg `0.0192` n `27`; metal avg `0.0297` n `20`; unknown avg `9.4105` n `1160`
- 4h: commodity avg `-0.2984` n `13`; crypto_alt avg `-1.0468` n `237`; crypto_major avg `-0.8599` n `8`; equity avg `-0.3023` n `154`; fx avg `-0.0196` n `6`; index avg `-0.039` n `27`; metal avg `-0.1206` n `20`; unknown avg `9.2574` n `1134`
- 24h: commodity avg `-0.3342` n `13`; crypto_alt avg `-0.7114` n `237`; crypto_major avg `-0.5053` n `8`; equity avg `0.4683` n `153`; fx avg `-0.0233` n `6`; index avg `-0.0982` n `27`; metal avg `0.0249` n `20`; unknown avg `703.031` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1834`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
