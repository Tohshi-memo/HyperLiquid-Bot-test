# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T02:22:21.666495+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.5212` n `228`; crypto_major avg `-0.3711` n `8`; equity avg `-0.1012` n `74`; fx avg `-0.0013` n `6`; index avg `-0.0144` n `23`; metal avg `0.0168` n `18`; unknown avg `-0.1674` n `516`
- 1h: commodity avg `-0.0662` n `12`; crypto_alt avg `-0.2063` n `228`; crypto_major avg `-0.357` n `8`; equity avg `-0.0043` n `74`; fx avg `-0.0016` n `6`; index avg `0.0581` n `23`; metal avg `0.1569` n `18`; unknown avg `-0.0667` n `516`
- 4h: commodity avg `-0.0226` n `12`; crypto_alt avg `1.9848` n `228`; crypto_major avg `1.6259` n `8`; equity avg `0.691` n `74`; fx avg `-0.0179` n `6`; index avg `0.0685` n `23`; metal avg `0.3063` n `18`; unknown avg `0.3937` n `515`
- 24h: commodity avg `0.0554` n `12`; crypto_alt avg `0.9915` n `228`; crypto_major avg `0.2484` n `8`; equity avg `1.3183` n `74`; fx avg `0.0384` n `6`; index avg `0.6155` n `23`; metal avg `0.0763` n `18`; unknown avg `1.2534` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
