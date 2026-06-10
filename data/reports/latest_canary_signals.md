# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T16:07:27.086523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0408` n `12`; crypto_alt avg `0.2148` n `228`; crypto_major avg `-0.1138` n `8`; equity avg `0.278` n `74`; fx avg `0.0035` n `6`; index avg `0.2132` n `23`; metal avg `0.1159` n `18`; unknown avg `-0.1382` n `548`
- 1h: commodity avg `0.6992` n `12`; crypto_alt avg `0.4784` n `228`; crypto_major avg `0.544` n `8`; equity avg `0.0368` n `74`; fx avg `-0.0252` n `6`; index avg `-0.1347` n `23`; metal avg `0.1468` n `18`; unknown avg `-0.1115` n `548`
- 4h: commodity avg `0.4602` n `12`; crypto_alt avg `2.341` n `228`; crypto_major avg `2.2397` n `8`; equity avg `1.7588` n `74`; fx avg `-0.018` n `6`; index avg `0.4709` n `23`; metal avg `0.9009` n `18`; unknown avg `0.4201` n `547`
- 24h: commodity avg `2.1456` n `12`; crypto_alt avg `2.0596` n `228`; crypto_major avg `0.9415` n `8`; equity avg `1.4924` n `74`; fx avg `-0.0974` n `6`; index avg `0.5333` n `23`; metal avg `-1.1112` n `18`; unknown avg `-0.0453` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0457`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.044`, n `668`, weak_sample_signal
