# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T20:22:31.630578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0229` n `12`; crypto_alt avg `-0.1528` n `232`; crypto_major avg `-0.2515` n `8`; equity avg `-0.067` n `133`; fx avg `0.0068` n `6`; index avg `-0.0059` n `26`; metal avg `-0.0175` n `20`; unknown avg `-0.3964` n `788`
- 1h: commodity avg `0.0323` n `12`; crypto_alt avg `-0.4181` n `232`; crypto_major avg `-0.1465` n `8`; equity avg `-0.012` n `133`; fx avg `0.0091` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0256` n `20`; unknown avg `23.5414` n `778`
- 4h: commodity avg `0.1099` n `12`; crypto_alt avg `0.5516` n `232`; crypto_major avg `0.5687` n `8`; equity avg `0.207` n `133`; fx avg `0.027` n `6`; index avg `0.0272` n `26`; metal avg `-0.0861` n `20`; unknown avg `1.21` n `778`
- 24h: commodity avg `-0.0553` n `12`; crypto_alt avg `4.2466` n `232`; crypto_major avg `5.3432` n `8`; equity avg `1.5911` n `133`; fx avg `-0.2192` n `6`; index avg `0.2022` n `26`; metal avg `0.7666` n `20`; unknown avg `26.206` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
