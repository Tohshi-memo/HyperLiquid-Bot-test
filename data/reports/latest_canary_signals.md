# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T07:52:25.933140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0129` n `12`; crypto_alt avg `-0.1365` n `228`; crypto_major avg `-0.1175` n `8`; equity avg `0.0067` n `78`; fx avg `0.2817` n `6`; index avg `-0.0134` n `23`; metal avg `0.0028` n `18`; unknown avg `-0.0366` n `687`
- 1h: commodity avg `0.0043` n `12`; crypto_alt avg `-0.2666` n `228`; crypto_major avg `-0.2133` n `8`; equity avg `-0.1017` n `78`; fx avg `-0.0139` n `6`; index avg `-0.0494` n `23`; metal avg `0.0266` n `18`; unknown avg `0.0339` n `687`
- 4h: commodity avg `0.0718` n `12`; crypto_alt avg `0.5859` n `228`; crypto_major avg `1.0629` n `8`; equity avg `0.2474` n `78`; fx avg `-0.0193` n `6`; index avg `-0.0164` n `23`; metal avg `0.0813` n `18`; unknown avg `0.0595` n `639`
- 24h: commodity avg `0.5285` n `12`; crypto_alt avg `-3.2236` n `228`; crypto_major avg `-3.4183` n `8`; equity avg `1.307` n `78`; fx avg `-0.1135` n `6`; index avg `0.2752` n `23`; metal avg `-4.0806` n `18`; unknown avg `0.1037` n `530`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
