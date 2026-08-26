# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T10:48:35.789029+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.025` n `12`; crypto_alt avg `0.2612` n `231`; crypto_major avg `0.2796` n `8`; equity avg `0.0205` n `122`; fx avg `0.0062` n `6`; index avg `0.0011` n `25`; metal avg `0.0046` n `20`; unknown avg `0.0473` n `797`
- 1h: commodity avg `0.0879` n `12`; crypto_alt avg `0.859` n `231`; crypto_major avg `1.0565` n `8`; equity avg `0.0667` n `122`; fx avg `-0.0126` n `6`; index avg `0.0001` n `25`; metal avg `0.0064` n `20`; unknown avg `0.2208` n `797`
- 4h: commodity avg `-0.0019` n `12`; crypto_alt avg `0.1737` n `231`; crypto_major avg `0.4673` n `8`; equity avg `-0.0489` n `122`; fx avg `-0.0043` n `6`; index avg `-0.0355` n `25`; metal avg `-0.0387` n `20`; unknown avg `0.1668` n `797`
- 24h: commodity avg `-0.2721` n `12`; crypto_alt avg `-1.4425` n `231`; crypto_major avg `-1.0324` n `8`; equity avg `0.1519` n `122`; fx avg `-0.026` n `6`; index avg `-0.0434` n `25`; metal avg `0.1371` n `20`; unknown avg `0.709` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.187`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
