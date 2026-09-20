# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T23:29:55.588586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0337` n `12`; crypto_alt avg `0.0874` n `234`; crypto_major avg `0.0744` n `8`; equity avg `0.0701` n `140`; fx avg `-0.0024` n `6`; index avg `0.004` n `26`; metal avg `-0.0083` n `20`; unknown avg `19.3498` n `943`
- 1h: commodity avg `-0.0692` n `12`; crypto_alt avg `-0.2264` n `234`; crypto_major avg `0.2227` n `8`; equity avg `0.2476` n `140`; fx avg `0.0043` n `6`; index avg `0.0446` n `26`; metal avg `-0.0091` n `20`; unknown avg `6.367` n `941`
- 4h: commodity avg `-0.314` n `12`; crypto_alt avg `0.7041` n `234`; crypto_major avg `0.4352` n `8`; equity avg `0.517` n `140`; fx avg `0.0742` n `6`; index avg `0.1084` n `26`; metal avg `0.0447` n `20`; unknown avg `2.4095` n `853`
- 24h: commodity avg `-0.0141` n `12`; crypto_alt avg `0.9763` n `234`; crypto_major avg `0.3418` n `8`; equity avg `0.403` n `140`; fx avg `0.0654` n `6`; index avg `0.0667` n `26`; metal avg `0.0214` n `20`; unknown avg `3.8075` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
