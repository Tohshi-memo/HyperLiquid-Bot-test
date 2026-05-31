# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T14:22:23.563966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `12`; crypto_alt avg `-0.7738` n `228`; crypto_major avg `-0.4093` n `8`; equity avg `-0.1063` n `69`; fx avg `-0.0042` n `6`; index avg `-0.0208` n `23`; metal avg `-0.0085` n `18`; unknown avg `-0.0851` n `421`
- 1h: commodity avg `0.0206` n `12`; crypto_alt avg `-1.315` n `228`; crypto_major avg `-0.7658` n `8`; equity avg `-0.1064` n `69`; fx avg `-0.005` n `6`; index avg `0.0062` n `23`; metal avg `-0.0253` n `18`; unknown avg `-0.3764` n `421`
- 4h: commodity avg `0.0715` n `12`; crypto_alt avg `-0.5597` n `228`; crypto_major avg `-0.2438` n `8`; equity avg `-0.0498` n `69`; fx avg `-0.0196` n `6`; index avg `-0.0838` n `23`; metal avg `-0.0076` n `18`; unknown avg `-0.3748` n `421`
- 24h: commodity avg `0.1092` n `12`; crypto_alt avg `-1.064` n `228`; crypto_major avg `0.4968` n `8`; equity avg `0.6623` n `69`; fx avg `-0.0214` n `6`; index avg `-0.2932` n `23`; metal avg `-0.0666` n `18`; unknown avg `0.1919` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
