# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T20:37:32.712168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.024` n `13`; crypto_alt avg `-0.0539` n `237`; crypto_major avg `-0.0068` n `8`; equity avg `-0.0281` n `152`; fx avg `-0.0158` n `6`; index avg `-0.0047` n `26`; metal avg `0.0006` n `20`; unknown avg `0.4449` n `1222`
- 1h: commodity avg `0.0433` n `13`; crypto_alt avg `-0.0938` n `237`; crypto_major avg `-0.0501` n `8`; equity avg `-0.0109` n `152`; fx avg `-0.0083` n `6`; index avg `-0.0051` n `26`; metal avg `0.015` n `20`; unknown avg `9.0595` n `1152`
- 4h: commodity avg `-0.0041` n `13`; crypto_alt avg `0.2861` n `237`; crypto_major avg `0.2293` n `8`; equity avg `0.1609` n `152`; fx avg `0.0141` n `6`; index avg `0.0228` n `26`; metal avg `0.0404` n `20`; unknown avg `3.6442` n `1152`
- 24h: commodity avg `-0.1949` n `13`; crypto_alt avg `-0.1735` n `237`; crypto_major avg `0.4861` n `8`; equity avg `0.5713` n `152`; fx avg `0.0351` n `6`; index avg `0.1201` n `26`; metal avg `0.1315` n `20`; unknown avg `0.6779` n `1015`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2276`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1686`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
