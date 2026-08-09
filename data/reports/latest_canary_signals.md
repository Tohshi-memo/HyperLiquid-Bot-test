# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T19:37:25.492787+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0186` n `12`; crypto_alt avg `0.0173` n `230`; crypto_major avg `0.0342` n `8`; equity avg `0.0077` n `112`; fx avg `-0.0039` n `6`; index avg `-0.0009` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0797` n `785`
- 1h: commodity avg `0.0495` n `12`; crypto_alt avg `0.0657` n `230`; crypto_major avg `0.04` n `8`; equity avg `-0.0042` n `112`; fx avg `-0.0038` n `6`; index avg `-0.0041` n `25`; metal avg `0.0085` n `20`; unknown avg `-0.2811` n `785`
- 4h: commodity avg `0.0597` n `12`; crypto_alt avg `0.501` n `230`; crypto_major avg `-0.083` n `8`; equity avg `0.1036` n `112`; fx avg `0.0052` n `6`; index avg `0.035` n `25`; metal avg `0.0078` n `20`; unknown avg `-0.38` n `785`
- 24h: commodity avg `0.1064` n `12`; crypto_alt avg `1.3599` n `230`; crypto_major avg `0.2398` n `8`; equity avg `0.1335` n `112`; fx avg `-0.0082` n `6`; index avg `0.0425` n `25`; metal avg `0.0769` n `20`; unknown avg `-0.2175` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
