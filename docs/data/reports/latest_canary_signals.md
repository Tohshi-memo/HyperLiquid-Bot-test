# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T20:52:33.729493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `13`; crypto_alt avg `0.1281` n `237`; crypto_major avg `0.1001` n `8`; equity avg `0.0086` n `152`; fx avg `0.0016` n `6`; index avg `0.0012` n `26`; metal avg `-0.0098` n `20`; unknown avg `0.5714` n `1231`
- 1h: commodity avg `0.0157` n `13`; crypto_alt avg `0.5576` n `237`; crypto_major avg `0.3175` n `8`; equity avg `0.066` n `152`; fx avg `0.0073` n `6`; index avg `0.0059` n `26`; metal avg `0.003` n `20`; unknown avg `0.1421` n `1199`
- 4h: commodity avg `-0.0106` n `13`; crypto_alt avg `1.0234` n `237`; crypto_major avg `0.9013` n `8`; equity avg `0.333` n `152`; fx avg `-0.0093` n `6`; index avg `0.0453` n `26`; metal avg `0.0348` n `20`; unknown avg `0.732` n `1165`
- 24h: commodity avg `0.0944` n `13`; crypto_alt avg `-2.122` n `237`; crypto_major avg `-1.5328` n `8`; equity avg `-0.2508` n `152`; fx avg `-0.0201` n `6`; index avg `-0.0538` n `26`; metal avg `-0.1301` n `20`; unknown avg `0.2797` n `1076`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1921`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1808`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
