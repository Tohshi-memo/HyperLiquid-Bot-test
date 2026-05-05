# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T20:56:31.314231+00:00`
- Correlation status: `ready`
- Asset price records: `391`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1005` n `7`; crypto_alt avg `0.2568` n `223`; crypto_major avg `0.068` n `7`; equity avg `-0.1969` n `47`; fx avg `-0.0347` n `4`; index avg `0.0163` n `6`; metal avg `-0.0729` n `7`; unknown avg `0.1609` n `313`
- 1h: commodity avg `0.0945` n `7`; crypto_alt avg `0.6959` n `223`; crypto_major avg `0.3076` n `7`; equity avg `0.1372` n `47`; fx avg `0.0014` n `4`; index avg `0.0978` n `6`; metal avg `-0.0024` n `7`; unknown avg `-0.0474` n `313`
- 4h: commodity avg `0.038` n `7`; crypto_alt avg `1.3883` n `223`; crypto_major avg `1.004` n `7`; equity avg `0.4647` n `47`; fx avg `0.01` n `4`; index avg `0.266` n `6`; metal avg `-0.2448` n `7`; unknown avg `0.2904` n `313`
- 24h: commodity avg `-1.0346` n `7`; crypto_alt avg `2.8349` n `223`; crypto_major avg `2.8173` n `7`; equity avg `2.157` n `47`; fx avg `-0.0508` n `4`; index avg `1.4421` n `6`; metal avg `0.6918` n `7`; unknown avg `1.3333` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2069`, n `387`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2`, n `387`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1309`, n `387`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1268`, n `387`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1133`, n `383`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `387`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1072`, n `387`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1055`, n `383`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1029`, n `387`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.102`, n `387`, weak_sample_signal
