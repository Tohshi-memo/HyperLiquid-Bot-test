# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T15:22:30.926146+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0617` n `12`; crypto_alt avg `0.1568` n `228`; crypto_major avg `0.2496` n `8`; equity avg `-0.055` n `74`; fx avg `0.0075` n `6`; index avg `-0.0635` n `23`; metal avg `0.1924` n `18`; unknown avg `-0.0281` n `517`
- 1h: commodity avg `0.1175` n `12`; crypto_alt avg `0.7672` n `228`; crypto_major avg `0.7909` n `8`; equity avg `1.1949` n `74`; fx avg `0.0127` n `6`; index avg `0.5001` n `23`; metal avg `0.6362` n `18`; unknown avg `-0.2227` n `517`
- 4h: commodity avg `0.1132` n `12`; crypto_alt avg `0.7549` n `228`; crypto_major avg `1.3027` n `8`; equity avg `1.2349` n `74`; fx avg `0.0006` n `6`; index avg `0.539` n `23`; metal avg `0.0166` n `18`; unknown avg `-2.04` n `517`
- 24h: commodity avg `-0.4386` n `12`; crypto_alt avg `2.6642` n `228`; crypto_major avg `4.1685` n `8`; equity avg `2.7986` n `74`; fx avg `-0.2588` n `6`; index avg `1.3935` n `23`; metal avg `0.2822` n `18`; unknown avg `-3.015` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
