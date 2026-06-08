# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T16:52:37.220161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0954` n `12`; crypto_alt avg `-0.1266` n `228`; crypto_major avg `-0.1143` n `8`; equity avg `0.1209` n `74`; fx avg `0.0048` n `6`; index avg `0.0962` n `23`; metal avg `0.0801` n `18`; unknown avg `0.0087` n `517`
- 1h: commodity avg `0.0373` n `12`; crypto_alt avg `-0.2025` n `228`; crypto_major avg `-0.5843` n `8`; equity avg `-0.0897` n `74`; fx avg `-0.0175` n `6`; index avg `-0.0793` n `23`; metal avg `0.0267` n `18`; unknown avg `-0.0273` n `517`
- 4h: commodity avg `0.0584` n `12`; crypto_alt avg `0.2266` n `228`; crypto_major avg `0.4612` n `8`; equity avg `0.6905` n `74`; fx avg `0.0106` n `6`; index avg `0.2155` n `23`; metal avg `0.0013` n `18`; unknown avg `0.0861` n `517`
- 24h: commodity avg `-0.5382` n `12`; crypto_alt avg `1.9111` n `228`; crypto_major avg `2.97` n `8`; equity avg `2.3468` n `74`; fx avg `-0.2747` n `6`; index avg `1.1059` n `23`; metal avg `0.1785` n `18`; unknown avg `-3.2165` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
