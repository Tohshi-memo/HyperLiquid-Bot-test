# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T16:37:22.699637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0246` n `12`; crypto_alt avg `0.2111` n `228`; crypto_major avg `0.0983` n `8`; equity avg `0.0468` n `74`; fx avg `0.0049` n `6`; index avg `0.0758` n `23`; metal avg `0.0316` n `18`; unknown avg `0.0958` n `516`
- 1h: commodity avg `0.1105` n `12`; crypto_alt avg `0.0604` n `228`; crypto_major avg `0.0573` n `8`; equity avg `0.144` n `74`; fx avg `-0.0023` n `6`; index avg `0.0471` n `23`; metal avg `0.0423` n `18`; unknown avg `0.0149` n `516`
- 4h: commodity avg `0.3023` n `12`; crypto_alt avg `1.3085` n `228`; crypto_major avg `1.1152` n `8`; equity avg `0.6921` n `74`; fx avg `-0.0041` n `6`; index avg `0.2467` n `23`; metal avg `0.1176` n `18`; unknown avg `0.5065` n `516`
- 24h: commodity avg `0.3311` n `12`; crypto_alt avg `3.1958` n `228`; crypto_major avg `3.4497` n `8`; equity avg `2.0724` n `74`; fx avg `-0.0172` n `6`; index avg `0.4088` n `23`; metal avg `0.6492` n `18`; unknown avg `-3.9092` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
