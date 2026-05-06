# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T07:13:06.125682+00:00`
- Correlation status: `ready`
- Asset price records: `432`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0445` n `7`; crypto_alt avg `0.321` n `223`; crypto_major avg `0.2359` n `7`; equity avg `-0.0588` n `47`; fx avg `0.0649` n `4`; index avg `-0.1225` n `6`; metal avg `-0.053` n `7`; unknown avg `0.2676` n `313`
- 1h: commodity avg `0.2939` n `7`; crypto_alt avg `0.5193` n `223`; crypto_major avg `0.3143` n `7`; equity avg `-0.1518` n `47`; fx avg `0.0572` n `4`; index avg `-0.1294` n `6`; metal avg `-0.1473` n `7`; unknown avg `0.6037` n `313`
- 4h: commodity avg `0.1508` n `7`; crypto_alt avg `0.5404` n `223`; crypto_major avg `0.4641` n `7`; equity avg `0.4886` n `47`; fx avg `-0.1549` n `4`; index avg `0.2188` n `6`; metal avg `0.2131` n `7`; unknown avg `1.0532` n `311`
- 24h: commodity avg `-1.4255` n `7`; crypto_alt avg `2.9904` n `223`; crypto_major avg `1.8265` n `7`; equity avg `2.4565` n `47`; fx avg `-0.3359` n `4`; index avg `1.9829` n `6`; metal avg `1.9124` n `7`; unknown avg `2.1094` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1806`, n `428`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1743`, n `428`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1272`, n `428`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1258`, n `428`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.122`, n `428`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.11`, n `428`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1013`, n `424`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0962`, n `424`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0949`, n `428`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0942`, n `428`, weak_sample_signal
