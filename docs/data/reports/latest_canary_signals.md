# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T18:00:39.509704+00:00`
- Correlation status: `ready`
- Asset price records: `380`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0492` n `7`; crypto_alt avg `0.0554` n `223`; crypto_major avg `0.0085` n `7`; equity avg `-0.0294` n `47`; fx avg `0.0339` n `4`; index avg `-0.0015` n `6`; metal avg `0.0133` n `7`; unknown avg `0.0547` n `313`
- 1h: commodity avg `-0.1525` n `7`; crypto_alt avg `0.1668` n `223`; crypto_major avg `0.3303` n `7`; equity avg `0.1114` n `47`; fx avg `0.0481` n `4`; index avg `0.106` n `6`; metal avg `-0.0624` n `7`; unknown avg `-0.0176` n `313`
- 4h: commodity avg `-0.2322` n `7`; crypto_alt avg `-0.1847` n `223`; crypto_major avg `0.2404` n `7`; equity avg `0.8813` n `47`; fx avg `-0.1055` n `4`; index avg `0.558` n `6`; metal avg `-0.557` n `7`; unknown avg `0.25` n `312`
- 24h: commodity avg `-1.2637` n `7`; crypto_alt avg `1.0376` n `223`; crypto_major avg `1.5538` n `7`; equity avg `1.5068` n `47`; fx avg `-0.0168` n `4`; index avg `1.4135` n `6`; metal avg `0.7844` n `7`; unknown avg `0.6779` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2071`, n `376`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2003`, n `376`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1326`, n `376`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1285`, n `376`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1128`, n `372`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1091`, n `376`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1058`, n `376`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `376`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1051`, n `372`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `376`, weak_sample_signal
