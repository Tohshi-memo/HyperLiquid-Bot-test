# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T12:22:25.856232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `0.1511` n `228`; crypto_major avg `0.0231` n `8`; equity avg `0.1022` n `74`; fx avg `-0.0156` n `6`; index avg `0.0408` n `23`; metal avg `-0.075` n `18`; unknown avg `-2.5689` n `517`
- 1h: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.5123` n `228`; crypto_major avg `-0.6766` n `8`; equity avg `0.1637` n `74`; fx avg `-0.0229` n `6`; index avg `0.1252` n `23`; metal avg `0.0768` n `18`; unknown avg `-2.6053` n `517`
- 4h: commodity avg `-1.0468` n `12`; crypto_alt avg `1.0578` n `228`; crypto_major avg `0.5693` n `8`; equity avg `0.9462` n `74`; fx avg `0.021` n `6`; index avg `0.6104` n `23`; metal avg `0.9897` n `18`; unknown avg `-2.2811` n `517`
- 24h: commodity avg `-0.3635` n `12`; crypto_alt avg `2.3368` n `228`; crypto_major avg `2.9106` n `8`; equity avg `2.1273` n `74`; fx avg `-0.277` n `6`; index avg `0.9982` n `23`; metal avg `0.3012` n `18`; unknown avg `-3.526` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
