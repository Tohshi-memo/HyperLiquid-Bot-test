# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T18:52:24.771570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `13`; crypto_alt avg `-0.0077` n `237`; crypto_major avg `-0.0066` n `8`; equity avg `0.0461` n `152`; fx avg `0.0057` n `6`; index avg `-0.0007` n `26`; metal avg `0.0021` n `20`; unknown avg `4.739` n `1240`
- 1h: commodity avg `-0.0634` n `13`; crypto_alt avg `-0.0645` n `237`; crypto_major avg `-0.1034` n `8`; equity avg `0.0631` n `152`; fx avg `-0.0029` n `6`; index avg `0.0095` n `26`; metal avg `-0.0067` n `20`; unknown avg `3.5781` n `1240`
- 4h: commodity avg `-0.0737` n `13`; crypto_alt avg `0.8795` n `237`; crypto_major avg `0.3761` n `8`; equity avg `0.3681` n `152`; fx avg `-0.0132` n `6`; index avg `0.0402` n `26`; metal avg `0.0458` n `20`; unknown avg `5.8293` n `1186`
- 24h: commodity avg `-0.2143` n `13`; crypto_alt avg `0.4455` n `237`; crypto_major avg `0.8909` n `8`; equity avg `0.774` n `152`; fx avg `0.0176` n `6`; index avg `0.1516` n `26`; metal avg `0.1659` n `20`; unknown avg `10.4551` n `1043`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2249`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1667`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
