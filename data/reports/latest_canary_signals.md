# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T09:07:15.148490+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.3898` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.2241` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `0.0204` n `228`; crypto_major avg `0.0474` n `8`; equity avg `0.0157` n `65`; fx avg `0.0` n `5`; index avg `0.0153` n `23`; metal avg `-0.008` n `18`; unknown avg `-0.0552` n `383`
- 1h: commodity avg `0.0582` n `12`; crypto_alt avg `-0.1392` n `228`; crypto_major avg `-0.0399` n `8`; equity avg `0.0426` n `65`; fx avg `0.0024` n `5`; index avg `0.0356` n `23`; metal avg `-0.0294` n `18`; unknown avg `-0.0916` n `383`
- 4h: commodity avg `1.7872` n `12`; crypto_alt avg `-8.9649` n `228`; crypto_major avg `-2.6026` n `8`; equity avg `-2.8307` n `65`; fx avg `-0.17` n `5`; index avg `-1.7749` n `23`; metal avg `-5.8267` n `18`; unknown avg `550.1361` n `367`
- 24h: commodity avg `1.7872` n `12`; crypto_alt avg `-8.9649` n `228`; crypto_major avg `-2.6026` n `8`; equity avg `-2.8307` n `65`; fx avg `-0.17` n `5`; index avg `-1.7749` n `23`; metal avg `-5.8267` n `18`; unknown avg `550.1361` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
