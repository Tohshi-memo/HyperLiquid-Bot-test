# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T12:22:29.438106+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.42` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.1414` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6053` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.01` n `12`; crypto_alt avg `-0.1452` n `228`; crypto_major avg `-0.0171` n `8`; equity avg `-0.1783` n `74`; fx avg `-0.01` n `6`; index avg `-0.0968` n `23`; metal avg `-0.286` n `18`; unknown avg `-0.0362` n `689`
- 1h: commodity avg `0.1781` n `12`; crypto_alt avg `-0.11` n `228`; crypto_major avg `0.1293` n `8`; equity avg `-0.2293` n `74`; fx avg `-0.0056` n `6`; index avg `-0.0671` n `23`; metal avg `-0.1112` n `18`; unknown avg `0.0084` n `689`
- 4h: commodity avg `0.0518` n `12`; crypto_alt avg `1.3428` n `228`; crypto_major avg `1.9146` n `8`; equity avg `-0.2268` n `74`; fx avg `0.0035` n `6`; index avg `0.0066` n `23`; metal avg `0.3093` n `18`; unknown avg `0.2682` n `689`
- 24h: commodity avg `-0.9252` n `12`; crypto_alt avg `4.2381` n `228`; crypto_major avg `4.714` n `8`; equity avg `1.4018` n `74`; fx avg `0.02` n `6`; index avg `0.8681` n `23`; metal avg `2.3633` n `18`; unknown avg `1.337` n `529`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
