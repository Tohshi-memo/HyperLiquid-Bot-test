# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T17:22:26.692948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `-0.077` n `228`; crypto_major avg `-0.0904` n `8`; equity avg `-0.0218` n `78`; fx avg `-0.0111` n `6`; index avg `-0.0106` n `23`; metal avg `0.0018` n `18`; unknown avg `0.7973` n `702`
- 1h: commodity avg `0.087` n `12`; crypto_alt avg `-0.0753` n `228`; crypto_major avg `-0.04` n `8`; equity avg `-0.0268` n `78`; fx avg `-0.0973` n `6`; index avg `0.0036` n `23`; metal avg `0.0001` n `18`; unknown avg `-0.5906` n `702`
- 4h: commodity avg `0.2765` n `12`; crypto_alt avg `0.1942` n `228`; crypto_major avg `0.2809` n `8`; equity avg `-0.0383` n `78`; fx avg `0.0203` n `6`; index avg `-0.011` n `23`; metal avg `-0.027` n `18`; unknown avg `-0.6539` n `702`
- 24h: commodity avg `0.1685` n `12`; crypto_alt avg `1.5964` n `228`; crypto_major avg `0.4058` n `8`; equity avg `0.3694` n `78`; fx avg `-0.0767` n `6`; index avg `0.0233` n `23`; metal avg `-0.0483` n `18`; unknown avg `-0.2608` n `653`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
