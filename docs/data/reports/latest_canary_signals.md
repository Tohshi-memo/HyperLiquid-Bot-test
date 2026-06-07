# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T05:07:21.643801+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `12`; crypto_alt avg `-0.1069` n `228`; crypto_major avg `0.0432` n `8`; equity avg `0.0603` n `74`; fx avg `0.0014` n `6`; index avg `-0.0238` n `23`; metal avg `0.037` n `18`; unknown avg `0.3637` n `516`
- 1h: commodity avg `-0.0285` n `12`; crypto_alt avg `0.0867` n `228`; crypto_major avg `0.5634` n `8`; equity avg `0.2733` n `74`; fx avg `-0.0014` n `6`; index avg `0.0112` n `23`; metal avg `0.0388` n `18`; unknown avg `0.0773` n `516`
- 4h: commodity avg `-0.1128` n `12`; crypto_alt avg `0.6769` n `228`; crypto_major avg `1.4702` n `8`; equity avg `0.645` n `74`; fx avg `0.0045` n `6`; index avg `0.4178` n `23`; metal avg `0.4441` n `18`; unknown avg `2.4037` n `516`
- 24h: commodity avg `0.3529` n `12`; crypto_alt avg `5.588` n `228`; crypto_major avg `4.3064` n `8`; equity avg `2.543` n `74`; fx avg `0.0487` n `6`; index avg `1.375` n `23`; metal avg `0.8712` n `18`; unknown avg `1.0178` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
