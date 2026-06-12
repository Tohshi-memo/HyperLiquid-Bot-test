# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T19:26:01.037501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.275` n `12`; crypto_alt avg `0.1122` n `228`; crypto_major avg `0.1088` n `8`; equity avg `-0.0571` n `74`; fx avg `-0.0102` n `6`; index avg `-0.041` n `23`; metal avg `-0.0832` n `18`; unknown avg `0.0403` n `643`
- 1h: commodity avg `-0.3174` n `12`; crypto_alt avg `0.3437` n `228`; crypto_major avg `0.0914` n `8`; equity avg `0.0673` n `74`; fx avg `-0.0088` n `6`; index avg `0.0761` n `23`; metal avg `-0.2339` n `18`; unknown avg `-0.1382` n `643`
- 4h: commodity avg `-0.0154` n `12`; crypto_alt avg `-0.9313` n `228`; crypto_major avg `-0.8009` n `8`; equity avg `-0.6549` n `74`; fx avg `0.0114` n `6`; index avg `-0.1554` n `23`; metal avg `0.1657` n `18`; unknown avg `-0.1086` n `643`
- 24h: commodity avg `-1.3345` n `12`; crypto_alt avg `0.1478` n `228`; crypto_major avg `0.591` n `8`; equity avg `0.3259` n `74`; fx avg `0.0135` n `6`; index avg `0.9091` n `23`; metal avg `0.6154` n `18`; unknown avg `40.3315` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
