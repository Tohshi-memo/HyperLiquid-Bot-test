# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T13:52:16.855918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.4045` n `12`; crypto_alt avg `-0.2273` n `228`; crypto_major avg `0.0296` n `8`; equity avg `-0.3255` n `67`; fx avg `0.0007` n `6`; index avg `0.0459` n `23`; metal avg `-0.1498` n `18`; unknown avg `0.9488` n `386`
- 1h: commodity avg `0.3573` n `12`; crypto_alt avg `-0.4939` n `228`; crypto_major avg `-0.1822` n `8`; equity avg `0.0873` n `67`; fx avg `-0.0049` n `6`; index avg `0.3161` n `23`; metal avg `-0.0341` n `18`; unknown avg `0.8631` n `386`
- 4h: commodity avg `-0.4926` n `12`; crypto_alt avg `0.3467` n `228`; crypto_major avg `0.6688` n `8`; equity avg `0.2607` n `67`; fx avg `-0.0321` n `6`; index avg `0.3725` n `23`; metal avg `-0.5224` n `18`; unknown avg `1.3663` n `386`
- 24h: commodity avg `-1.2454` n `12`; crypto_alt avg `2.4899` n `228`; crypto_major avg `1.2477` n `8`; equity avg `1.3146` n `67`; fx avg `0.1298` n `6`; index avg `1.0627` n `23`; metal avg `0.2995` n `18`; unknown avg `2.4158` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0427`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0414`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0406`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0404`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0381`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0374`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0358`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0334`, n `668`, weak_sample_signal
