# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T08:30:25.392465+00:00`
- Correlation status: `ready`
- Asset price records: `438`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1145` n `7`; crypto_alt avg `0.2392` n `223`; crypto_major avg `0.1091` n `7`; equity avg `0.1292` n `47`; fx avg `-0.0059` n `4`; index avg `0.2633` n `6`; metal avg `-0.0547` n `7`; unknown avg `-0.0226` n `313`
- 1h: commodity avg `-0.3906` n `7`; crypto_alt avg `0.4881` n `223`; crypto_major avg `0.204` n `7`; equity avg `0.3153` n `47`; fx avg `-0.0977` n `4`; index avg `0.2236` n `6`; metal avg `0.2863` n `7`; unknown avg `0.0138` n `313`
- 4h: commodity avg `-0.3629` n `7`; crypto_alt avg `1.3579` n `223`; crypto_major avg `0.8603` n `7`; equity avg `0.3427` n `47`; fx avg `-0.101` n `4`; index avg `0.2619` n `6`; metal avg `0.2998` n `7`; unknown avg `1.2119` n `311`
- 24h: commodity avg `-1.6706` n `7`; crypto_alt avg `3.1965` n `223`; crypto_major avg `2.2284` n `7`; equity avg `2.8286` n `47`; fx avg `-0.4753` n `4`; index avg `2.1596` n `6`; metal avg `2.099` n `7`; unknown avg `1.988` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1781`, n `434`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1718`, n `434`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1333`, n `434`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1246`, n `434`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1208`, n `434`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `434`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0977`, n `430`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0927`, n `430`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `434`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `434`, weak_sample_signal
