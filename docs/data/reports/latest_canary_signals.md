# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T06:52:27.080146+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `12`; crypto_alt avg `-0.2779` n `228`; crypto_major avg `-0.28` n `8`; equity avg `0.0564` n `74`; fx avg `0.0194` n `6`; index avg `0.0535` n `23`; metal avg `0.1154` n `18`; unknown avg `-0.1997` n `556`
- 1h: commodity avg `-0.0414` n `12`; crypto_alt avg `0.0992` n `228`; crypto_major avg `0.2003` n `8`; equity avg `0.2158` n `74`; fx avg `0.0357` n `6`; index avg `0.1026` n `23`; metal avg `-0.0827` n `18`; unknown avg `-0.2271` n `538`
- 4h: commodity avg `-0.4943` n `12`; crypto_alt avg `1.4628` n `228`; crypto_major avg `1.1987` n `8`; equity avg `0.8667` n `74`; fx avg `0.0433` n `6`; index avg `0.4222` n `23`; metal avg `0.8217` n `18`; unknown avg `0.1334` n `538`
- 24h: commodity avg `1.3013` n `12`; crypto_alt avg `1.045` n `228`; crypto_major avg `1.135` n `8`; equity avg `-0.4691` n `74`; fx avg `0.0669` n `6`; index avg `-0.5461` n `23`; metal avg `-0.9085` n `18`; unknown avg `3.4914` n `535`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
