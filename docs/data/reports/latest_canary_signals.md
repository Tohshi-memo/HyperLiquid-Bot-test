# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T11:52:34.610263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.48` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.0474` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.0184` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0595` n `12`; crypto_alt avg `-0.0465` n `228`; crypto_major avg `0.137` n `8`; equity avg `0.0507` n `74`; fx avg `-0.0045` n `6`; index avg `0.0288` n `23`; metal avg `-0.104` n `18`; unknown avg `-0.0436` n `689`
- 1h: commodity avg `-0.001` n `12`; crypto_alt avg `1.1688` n `228`; crypto_major avg `1.4181` n `8`; equity avg `0.1394` n `74`; fx avg `0.0053` n `6`; index avg `0.0795` n `23`; metal avg `0.1608` n `18`; unknown avg `-0.1615` n `689`
- 4h: commodity avg `0.0798` n `12`; crypto_alt avg `1.5173` n `228`; crypto_major avg `2.0982` n `8`; equity avg `0.0508` n `74`; fx avg `-0.0002` n `6`; index avg `0.1198` n `23`; metal avg `0.6495` n `18`; unknown avg `0.8826` n `689`
- 24h: commodity avg `-1.0824` n `12`; crypto_alt avg `4.4158` n `228`; crypto_major avg `4.7318` n `8`; equity avg `1.4648` n `74`; fx avg `0.0514` n `6`; index avg `0.9678` n `23`; metal avg `2.5682` n `18`; unknown avg `1.1137` n `529`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
