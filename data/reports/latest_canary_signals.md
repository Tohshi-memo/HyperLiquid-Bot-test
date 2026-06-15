# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T08:37:28.957408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.56` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.2069` n `12`; crypto_alt avg `0.1855` n `228`; crypto_major avg `0.2506` n `8`; equity avg `0.1006` n `74`; fx avg `-0.0096` n `6`; index avg `0.043` n `23`; metal avg `0.2744` n `18`; unknown avg `0.0343` n `689`
- 1h: commodity avg `0.0543` n `12`; crypto_alt avg `0.193` n `228`; crypto_major avg `0.3052` n `8`; equity avg `0.2004` n `74`; fx avg `-0.0183` n `6`; index avg `0.0784` n `23`; metal avg `0.5426` n `18`; unknown avg `0.7377` n `689`
- 4h: commodity avg `-0.3163` n `12`; crypto_alt avg `0.412` n `228`; crypto_major avg `0.3407` n `8`; equity avg `0.195` n `74`; fx avg `-0.0105` n `6`; index avg `0.2837` n `23`; metal avg `0.244` n `18`; unknown avg `0.8408` n `529`
- 24h: commodity avg `-0.9733` n `12`; crypto_alt avg `2.8858` n `228`; crypto_major avg `3.0609` n `8`; equity avg `1.8257` n `74`; fx avg `0.0374` n `6`; index avg `1.0245` n `23`; metal avg `2.2844` n `18`; unknown avg `1.7486` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
