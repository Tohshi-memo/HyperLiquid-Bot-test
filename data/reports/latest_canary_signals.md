# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T17:53:02.313038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.26` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.6604` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0458` n `12`; crypto_alt avg `0.0684` n `228`; crypto_major avg `0.0084` n `8`; equity avg `0.0257` n `77`; fx avg `-0.0014` n `6`; index avg `-0.0216` n `23`; metal avg `-0.0363` n `18`; unknown avg `0.905` n `687`
- 1h: commodity avg `0.0995` n `12`; crypto_alt avg `-0.2105` n `228`; crypto_major avg `-0.4272` n `8`; equity avg `0.1666` n `77`; fx avg `0.0057` n `6`; index avg `-0.012` n `23`; metal avg `-0.2305` n `18`; unknown avg `1.8188` n `687`
- 4h: commodity avg `0.4163` n `12`; crypto_alt avg `-0.1457` n `228`; crypto_major avg `0.7907` n `8`; equity avg `0.8195` n `77`; fx avg `-0.0111` n `6`; index avg `0.0063` n `23`; metal avg `-0.8697` n `18`; unknown avg `4.8741` n `687`
- 24h: commodity avg `-0.6182` n `12`; crypto_alt avg `6.3682` n `228`; crypto_major avg `7.4737` n `8`; equity avg `3.2087` n `76`; fx avg `0.0725` n `6`; index avg `1.3025` n `23`; metal avg `2.2345` n `18`; unknown avg `6.0135` n `527`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
