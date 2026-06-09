# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T06:22:22.120192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1198` n `12`; crypto_alt avg `0.2879` n `228`; crypto_major avg `0.1495` n `8`; equity avg `0.086` n `74`; fx avg `0.0387` n `6`; index avg `0.071` n `23`; metal avg `0.0518` n `18`; unknown avg `0.0072` n `545`
- 1h: commodity avg `-0.238` n `12`; crypto_alt avg `0.3345` n `228`; crypto_major avg `0.328` n `8`; equity avg `0.4007` n `74`; fx avg `-0.0156` n `6`; index avg `0.1773` n `23`; metal avg `0.4054` n `18`; unknown avg `0.109` n `503`
- 4h: commodity avg `-0.4162` n `12`; crypto_alt avg `1.8102` n `228`; crypto_major avg `1.4876` n `8`; equity avg `1.311` n `74`; fx avg `-0.0237` n `6`; index avg `0.6005` n `23`; metal avg `0.5221` n `18`; unknown avg `0.3739` n `503`
- 24h: commodity avg `-1.5458` n `12`; crypto_alt avg `0.8975` n `228`; crypto_major avg `1.2785` n `8`; equity avg `3.44` n `74`; fx avg `-0.1739` n `6`; index avg `1.4258` n `23`; metal avg `0.7799` n `18`; unknown avg `-3.0132` n `503`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
