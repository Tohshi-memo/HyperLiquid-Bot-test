# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T04:41:30.245262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0271` n `12`; crypto_alt avg `0.8565` n `228`; crypto_major avg `0.9461` n `8`; equity avg `0.2252` n `74`; fx avg `0.0248` n `6`; index avg `0.0644` n `23`; metal avg `-0.0315` n `18`; unknown avg `0.7197` n `517`
- 1h: commodity avg `0.0178` n `12`; crypto_alt avg `1.4109` n `228`; crypto_major avg `1.0276` n `8`; equity avg `0.6013` n `74`; fx avg `0.0001` n `6`; index avg `0.2784` n `23`; metal avg `-0.035` n `18`; unknown avg `0.6057` n `517`
- 4h: commodity avg `-0.1546` n `12`; crypto_alt avg `0.9042` n `228`; crypto_major avg `0.9336` n `8`; equity avg `1.3946` n `74`; fx avg `-0.0015` n `6`; index avg `0.7277` n `23`; metal avg `0.2593` n `18`; unknown avg `0.0895` n `517`
- 24h: commodity avg `-1.3379` n `12`; crypto_alt avg `0.9211` n `228`; crypto_major avg `1.557` n `8`; equity avg `2.3961` n `74`; fx avg `-0.2981` n `6`; index avg `1.0643` n `23`; metal avg `0.1175` n `18`; unknown avg `-2.8865` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
