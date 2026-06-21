# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T19:07:43.849734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0288` n `12`; crypto_alt avg `0.1177` n `228`; crypto_major avg `-0.0249` n `8`; equity avg `-0.0154` n `78`; fx avg `-0.0031` n `6`; index avg `0.0036` n `23`; metal avg `-0.0064` n `18`; unknown avg `3.142` n `702`
- 1h: commodity avg `0.0758` n `12`; crypto_alt avg `0.4` n `228`; crypto_major avg `0.3613` n `8`; equity avg `0.0321` n `78`; fx avg `-0.0124` n `6`; index avg `0.001` n `23`; metal avg `0.0078` n `18`; unknown avg `0.302` n `702`
- 4h: commodity avg `0.1964` n `12`; crypto_alt avg `-0.0658` n `228`; crypto_major avg `-0.0906` n `8`; equity avg `-0.0314` n `78`; fx avg `-0.0971` n `6`; index avg `-0.0248` n `23`; metal avg `-0.0848` n `18`; unknown avg `-0.5768` n `702`
- 24h: commodity avg `0.2834` n `12`; crypto_alt avg `1.7434` n `228`; crypto_major avg `0.5297` n `8`; equity avg `0.4413` n `78`; fx avg `-0.0707` n `6`; index avg `0.0141` n `23`; metal avg `-0.1036` n `18`; unknown avg `-0.2613` n `653`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
