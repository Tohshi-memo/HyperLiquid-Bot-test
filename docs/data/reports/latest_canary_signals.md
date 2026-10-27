# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T15:53:05.604256+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.059` n `13`; crypto_alt avg `0.1573` n `238`; crypto_major avg `0.123` n `8`; equity avg `0.2159` n `154`; fx avg `-0.0031` n `6`; index avg `0.0455` n `27`; metal avg `0.034` n `20`; unknown avg `0.1102` n `1236`
- 1h: commodity avg `0.0766` n `13`; crypto_alt avg `0.59` n `238`; crypto_major avg `0.477` n `8`; equity avg `0.5261` n `154`; fx avg `-0.0084` n `6`; index avg `0.1322` n `27`; metal avg `0.0692` n `20`; unknown avg `7.7367` n `1202`
- 4h: commodity avg `-0.2067` n `13`; crypto_alt avg `1.3476` n `238`; crypto_major avg `1.2206` n `8`; equity avg `1.5332` n `154`; fx avg `-0.0106` n `6`; index avg `0.2295` n `27`; metal avg `0.4269` n `20`; unknown avg `1.5217` n `1150`
- 24h: commodity avg `-0.6289` n `13`; crypto_alt avg `-0.0252` n `237`; crypto_major avg `0.5429` n `8`; equity avg `1.377` n `154`; fx avg `-0.0722` n `6`; index avg `0.4019` n `27`; metal avg `0.1174` n `20`; unknown avg `26.754` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2279`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1996`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
