# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T15:07:26.836743+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.2971` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.2033` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0027` n `13`; crypto_alt avg `-0.486` n `237`; crypto_major avg `-0.6713` n `8`; equity avg `-0.1532` n `152`; fx avg `0.0059` n `6`; index avg `-0.0157` n `26`; metal avg `-0.0034` n `20`; unknown avg `-0.2089` n `1228`
- 1h: commodity avg `0.0253` n `13`; crypto_alt avg `-1.3351` n `237`; crypto_major avg `-1.3492` n `8`; equity avg `-0.3879` n `152`; fx avg `0.0067` n `6`; index avg `-0.0521` n `26`; metal avg `-0.0963` n `20`; unknown avg `1.6221` n `1228`
- 4h: commodity avg `0.1051` n `13`; crypto_alt avg `-1.666` n `237`; crypto_major avg `-1.2554` n `8`; equity avg `-0.3201` n `152`; fx avg `-0.016` n `6`; index avg `-0.0521` n `26`; metal avg `-0.0781` n `20`; unknown avg `0.6293` n `1190`
- 24h: commodity avg `0.3872` n `13`; crypto_alt avg `-4.1818` n `237`; crypto_major avg `-3.3582` n `8`; equity avg `-1.1068` n `152`; fx avg `-0.0347` n `6`; index avg `-0.1417` n `26`; metal avg `-0.2267` n `20`; unknown avg `-0.7207` n `1043`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1916`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
