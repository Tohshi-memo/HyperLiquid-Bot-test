# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T01:07:32.057512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0243` n `12`; crypto_alt avg `-0.2942` n `232`; crypto_major avg `-0.1808` n `8`; equity avg `-0.027` n `133`; fx avg `0.0285` n `6`; index avg `-0.0082` n `26`; metal avg `-0.0853` n `20`; unknown avg `-0.0231` n `791`
- 1h: commodity avg `-0.0273` n `12`; crypto_alt avg `-0.2577` n `232`; crypto_major avg `-0.1816` n `8`; equity avg `0.1603` n `133`; fx avg `0.079` n `6`; index avg `0.0151` n `26`; metal avg `-0.0903` n `20`; unknown avg `2.672` n `784`
- 4h: commodity avg `-0.0281` n `12`; crypto_alt avg `-0.6638` n `232`; crypto_major avg `-0.4354` n `8`; equity avg `0.3246` n `133`; fx avg `0.0386` n `6`; index avg `0.022` n `26`; metal avg `-0.0677` n `20`; unknown avg `2.2972` n `778`
- 24h: commodity avg `-0.1224` n `12`; crypto_alt avg `3.482` n `232`; crypto_major avg `4.8298` n `8`; equity avg `1.5138` n `133`; fx avg `-0.1865` n `6`; index avg `0.2036` n `26`; metal avg `0.6783` n `20`; unknown avg `23.4271` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
