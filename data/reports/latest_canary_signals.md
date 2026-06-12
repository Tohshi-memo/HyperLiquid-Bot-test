# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T05:07:27.171072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.125` n `12`; crypto_alt avg `-0.2423` n `228`; crypto_major avg `-0.1964` n `8`; equity avg `-0.0993` n `74`; fx avg `0.0043` n `6`; index avg `-0.0414` n `23`; metal avg `-0.0847` n `18`; unknown avg `0.3521` n `557`
- 1h: commodity avg `0.1332` n `12`; crypto_alt avg `0.1102` n `228`; crypto_major avg `0.1255` n `8`; equity avg `0.0783` n `74`; fx avg `0.0009` n `6`; index avg `0.073` n `23`; metal avg `-0.079` n `18`; unknown avg `2.5379` n `557`
- 4h: commodity avg `-0.1094` n `12`; crypto_alt avg `0.1448` n `228`; crypto_major avg `0.1834` n `8`; equity avg `-0.0403` n `74`; fx avg `0.0571` n `6`; index avg `0.0198` n `23`; metal avg `0.2046` n `18`; unknown avg `2.4314` n `556`
- 24h: commodity avg `-2.275` n `12`; crypto_alt avg `1.6798` n `228`; crypto_major avg `2.4876` n `8`; equity avg `3.7085` n `74`; fx avg `0.0387` n `6`; index avg `1.9774` n `23`; metal avg `3.0187` n `18`; unknown avg `1.7679` n `530`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
