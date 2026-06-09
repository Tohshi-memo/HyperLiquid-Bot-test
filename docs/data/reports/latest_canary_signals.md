# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T14:37:29.821286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0621` n `12`; crypto_alt avg `-0.1938` n `228`; crypto_major avg `-0.3217` n `8`; equity avg `0.0432` n `74`; fx avg `0.0055` n `6`; index avg `-0.1418` n `23`; metal avg `-0.4578` n `18`; unknown avg `-0.1795` n `547`
- 1h: commodity avg `-0.0033` n `12`; crypto_alt avg `-1.073` n `228`; crypto_major avg `-1.1499` n `8`; equity avg `-0.9906` n `74`; fx avg `0.0019` n `6`; index avg `-0.7288` n `23`; metal avg `-1.1042` n `18`; unknown avg `-0.2089` n `545`
- 4h: commodity avg `-0.4791` n `12`; crypto_alt avg `-0.8778` n `228`; crypto_major avg `-1.7396` n `8`; equity avg `-1.2271` n `74`; fx avg `0.0469` n `6`; index avg `-0.853` n `23`; metal avg `-1.0468` n `18`; unknown avg `-0.4597` n `545`
- 24h: commodity avg `-1.0085` n `12`; crypto_alt avg `-2.4979` n `228`; crypto_major avg `-2.9294` n `8`; equity avg `-0.6215` n `74`; fx avg `0.1391` n `6`; index avg `-0.359` n `23`; metal avg `-0.128` n `18`; unknown avg `-1.2425` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
