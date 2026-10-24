# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T16:52:26.981504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0252` n `13`; crypto_alt avg `0.8084` n `237`; crypto_major avg `0.688` n `8`; equity avg `0.2903` n `152`; fx avg `0.0031` n `6`; index avg `0.0348` n `26`; metal avg `0.0335` n `20`; unknown avg `1.4076` n `1223`
- 1h: commodity avg `-0.0278` n `13`; crypto_alt avg `0.8964` n `237`; crypto_major avg `0.8` n `8`; equity avg `0.3045` n `152`; fx avg `0.0062` n `6`; index avg `0.0364` n `26`; metal avg `0.0313` n `20`; unknown avg `0.9059` n `1217`
- 4h: commodity avg `-0.0271` n `13`; crypto_alt avg `-1.4916` n `237`; crypto_major avg `-0.9394` n `8`; equity avg `-0.3582` n `152`; fx avg `-0.0233` n `6`; index avg `-0.0601` n `26`; metal avg `-0.1042` n `20`; unknown avg `0.9679` n `1184`
- 24h: commodity avg `0.2454` n `13`; crypto_alt avg `-4.1175` n `237`; crypto_major avg `-2.9332` n `8`; equity avg `-0.8947` n `152`; fx avg `-0.0475` n `6`; index avg `-0.0989` n `26`; metal avg `-0.2743` n `20`; unknown avg `-0.9795` n `1061`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1914`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
