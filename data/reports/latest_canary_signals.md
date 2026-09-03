# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T22:22:25.350546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0253` n `12`; crypto_alt avg `0.0665` n `232`; crypto_major avg `-0.0516` n `8`; equity avg `-0.0277` n `133`; fx avg `-0.0012` n `6`; index avg `0.0056` n `26`; metal avg `-0.0065` n `20`; unknown avg `0.0499` n `786`
- 1h: commodity avg `-0.0036` n `12`; crypto_alt avg `-0.1437` n `232`; crypto_major avg `-0.1927` n `8`; equity avg `-0.0581` n `133`; fx avg `0.0008` n `6`; index avg `0.0043` n `26`; metal avg `0.0141` n `20`; unknown avg `2.17` n `784`
- 4h: commodity avg `0.1246` n `12`; crypto_alt avg `-0.0652` n `232`; crypto_major avg `0.0985` n `8`; equity avg `-0.1398` n `133`; fx avg `0.0153` n `6`; index avg `-0.0288` n `26`; metal avg `-0.0594` n `20`; unknown avg `3.1428` n `766`
- 24h: commodity avg `-0.0798` n `12`; crypto_alt avg `4.7239` n `232`; crypto_major avg `5.5983` n `8`; equity avg `1.2296` n `133`; fx avg `-0.2183` n `6`; index avg `0.1736` n `26`; metal avg `0.8189` n `20`; unknown avg `3.3309` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
