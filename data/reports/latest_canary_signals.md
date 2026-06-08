# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T20:37:38.980411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0461` n `12`; crypto_alt avg `0.1072` n `228`; crypto_major avg `0.0681` n `8`; equity avg `0.0893` n `74`; fx avg `-0.0086` n `6`; index avg `0.0171` n `23`; metal avg `0.1011` n `18`; unknown avg `-0.0914` n `517`
- 1h: commodity avg `-0.0923` n `12`; crypto_alt avg `-0.4755` n `228`; crypto_major avg `-0.3939` n `8`; equity avg `0.097` n `74`; fx avg `-0.007` n `6`; index avg `0.1362` n `23`; metal avg `-0.0161` n `18`; unknown avg `-0.1898` n `517`
- 4h: commodity avg `-0.0013` n `12`; crypto_alt avg `-0.1979` n `228`; crypto_major avg `-0.148` n `8`; equity avg `-0.4662` n `74`; fx avg `-0.0236` n `6`; index avg `-0.2513` n `23`; metal avg `-0.3051` n `18`; unknown avg `-0.2022` n `517`
- 24h: commodity avg `-0.793` n `12`; crypto_alt avg `3.1765` n `228`; crypto_major avg `3.4906` n `8`; equity avg `2.5515` n `74`; fx avg `-0.3138` n `6`; index avg `0.9976` n `23`; metal avg `0.0799` n `18`; unknown avg `-2.1451` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
