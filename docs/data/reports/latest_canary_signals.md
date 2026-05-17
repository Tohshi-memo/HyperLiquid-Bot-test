# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T14:22:14.354305+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0377` n `12`; crypto_alt avg `-0.2437` n `228`; crypto_major avg `-0.1658` n `8`; equity avg `-0.1576` n `65`; fx avg `0.0` n `5`; index avg `-0.0749` n `23`; metal avg `-0.0107` n `18`; unknown avg `0.045` n `383`
- 1h: commodity avg `-0.2456` n `12`; crypto_alt avg `-0.3` n `228`; crypto_major avg `-0.2089` n `8`; equity avg `-0.1349` n `65`; fx avg `0.0` n `5`; index avg `-0.0` n `23`; metal avg `-0.0043` n `18`; unknown avg `-0.0181` n `383`
- 4h: commodity avg `-0.2188` n `12`; crypto_alt avg `-1.1303` n `228`; crypto_major avg `-0.6174` n `8`; equity avg `-0.0236` n `65`; fx avg `-0.0175` n `5`; index avg `0.0591` n `23`; metal avg `0.0115` n `18`; unknown avg `-0.2069` n `383`
- 24h: commodity avg `1.5737` n `12`; crypto_alt avg `-9.5986` n `228`; crypto_major avg `-2.7365` n `8`; equity avg `-2.7013` n `65`; fx avg `-0.1861` n `5`; index avg `-1.6336` n `23`; metal avg `-5.8351` n `18`; unknown avg `549.9366` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
