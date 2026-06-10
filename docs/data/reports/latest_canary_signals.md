# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T15:54:03.392090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.8345` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.5055` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.6371` n `12`; crypto_alt avg `-0.1069` n `228`; crypto_major avg `0.2319` n `8`; equity avg `0.071` n `74`; fx avg `-0.0203` n `6`; index avg `0.0305` n `23`; metal avg `0.0076` n `18`; unknown avg `-0.0355` n `548`
- 1h: commodity avg `0.4739` n `12`; crypto_alt avg `0.4996` n `228`; crypto_major avg `0.7335` n `8`; equity avg `-0.772` n `74`; fx avg `-0.0247` n `6`; index avg `-0.6158` n `23`; metal avg `-0.137` n `18`; unknown avg `-0.0389` n `548`
- 4h: commodity avg `0.3254` n `12`; crypto_alt avg `2.0291` n `228`; crypto_major avg `2.1973` n `8`; equity avg `1.4766` n `74`; fx avg `-0.0225` n `6`; index avg `0.2311` n `23`; metal avg `0.3628` n `18`; unknown avg `1.6544` n `547`
- 24h: commodity avg `1.8932` n `12`; crypto_alt avg `1.0903` n `228`; crypto_major avg `0.5295` n `8`; equity avg `0.0664` n `74`; fx avg `-0.0934` n `6`; index avg `-0.2232` n `23`; metal avg `-1.4838` n `18`; unknown avg `-0.1739` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0477`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
