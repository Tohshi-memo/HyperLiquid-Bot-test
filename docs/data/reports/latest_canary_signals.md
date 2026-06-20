# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T09:07:31.177886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `0.2012` n `228`; crypto_major avg `0.1348` n `8`; equity avg `0.0281` n `78`; fx avg `-0.2858` n `6`; index avg `0.0084` n `23`; metal avg `0.0042` n `18`; unknown avg `0.0547` n `687`
- 1h: commodity avg `-0.0181` n `12`; crypto_alt avg `0.3408` n `228`; crypto_major avg `0.0963` n `8`; equity avg `-0.073` n `78`; fx avg `-0.2942` n `6`; index avg `0.009` n `23`; metal avg `-0.0359` n `18`; unknown avg `0.0836` n `687`
- 4h: commodity avg `0.0766` n `12`; crypto_alt avg `0.1832` n `228`; crypto_major avg `0.2977` n `8`; equity avg `0.0242` n `78`; fx avg `-0.2768` n `6`; index avg `-0.0181` n `23`; metal avg `0.0056` n `18`; unknown avg `-0.011` n `639`
- 24h: commodity avg `0.5015` n `12`; crypto_alt avg `-3.0289` n `228`; crypto_major avg `-3.4755` n `8`; equity avg `1.2352` n `78`; fx avg `-0.3806` n `6`; index avg `0.2795` n `23`; metal avg `-4.1088` n `18`; unknown avg `0.0662` n `530`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
