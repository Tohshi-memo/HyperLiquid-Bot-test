# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T19:52:28.784812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0235` n `13`; crypto_alt avg `-0.0494` n `237`; crypto_major avg `-0.0148` n `8`; equity avg `-0.0103` n `152`; fx avg `-0.0055` n `6`; index avg `-0.0003` n `26`; metal avg `0.0071` n `20`; unknown avg `6.8013` n `1218`
- 1h: commodity avg `-0.0073` n `13`; crypto_alt avg `-0.2398` n `237`; crypto_major avg `-0.0512` n `8`; equity avg `-0.041` n `152`; fx avg `0.0102` n `6`; index avg `0.0061` n `26`; metal avg `-0.0056` n `20`; unknown avg `6.2193` n `1200`
- 4h: commodity avg `-0.0682` n `13`; crypto_alt avg `0.0445` n `237`; crypto_major avg `0.1058` n `8`; equity avg `0.2454` n `152`; fx avg `0.0032` n `6`; index avg `0.0415` n `26`; metal avg `0.0462` n `20`; unknown avg `1.1042` n `1174`
- 24h: commodity avg `-0.197` n `13`; crypto_alt avg `0.297` n `237`; crypto_major avg `0.7403` n `8`; equity avg `0.6304` n `152`; fx avg `0.0436` n `6`; index avg `0.1297` n `26`; metal avg `0.1365` n `20`; unknown avg `10.2987` n `1029`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2259`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
