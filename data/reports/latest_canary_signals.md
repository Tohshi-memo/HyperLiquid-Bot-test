# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T06:22:24.000129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `0.2891` n `228`; crypto_major avg `0.1735` n `8`; equity avg `0.1088` n `74`; fx avg `-0.0007` n `6`; index avg `0.0136` n `23`; metal avg `0.0606` n `18`; unknown avg `5.8235` n `516`
- 1h: commodity avg `-0.0361` n `12`; crypto_alt avg `0.3804` n `228`; crypto_major avg `0.1608` n `8`; equity avg `0.1294` n `74`; fx avg `-0.0108` n `6`; index avg `0.0417` n `23`; metal avg `0.0372` n `18`; unknown avg `-0.1427` n `506`
- 4h: commodity avg `-0.0796` n `12`; crypto_alt avg `0.6228` n `228`; crypto_major avg `1.3248` n `8`; equity avg `0.6525` n `74`; fx avg `-0.0025` n `6`; index avg `0.3622` n `23`; metal avg `0.3078` n `18`; unknown avg `0.0143` n `506`
- 24h: commodity avg `0.3105` n `12`; crypto_alt avg `2.393` n `228`; crypto_major avg `1.2646` n `8`; equity avg `1.6494` n `74`; fx avg `0.0429` n `6`; index avg `0.948` n `23`; metal avg `0.5674` n `18`; unknown avg `1.847` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
