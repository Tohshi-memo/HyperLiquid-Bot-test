# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T19:22:29.247523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0288` n `12`; crypto_alt avg `-0.2501` n `234`; crypto_major avg `-0.2345` n `8`; equity avg `-0.0605` n `142`; fx avg `0.0036` n `6`; index avg `0.0024` n `26`; metal avg `0.0352` n `20`; unknown avg `0.3457` n `969`
- 1h: commodity avg `-0.0907` n `12`; crypto_alt avg `-0.5657` n `234`; crypto_major avg `-0.2685` n `8`; equity avg `0.083` n `142`; fx avg `-0.0046` n `6`; index avg `0.0024` n `26`; metal avg `0.077` n `20`; unknown avg `4.8379` n `967`
- 4h: commodity avg `-0.2396` n `12`; crypto_alt avg `-0.5374` n `234`; crypto_major avg `0.2304` n `8`; equity avg `0.0318` n `142`; fx avg `-0.038` n `6`; index avg `-0.0519` n `26`; metal avg `0.0606` n `20`; unknown avg `4.432` n `961`
- 24h: commodity avg `0.2642` n `12`; crypto_alt avg `-0.2575` n `234`; crypto_major avg `0.323` n `8`; equity avg `-0.1817` n `142`; fx avg `0.0584` n `6`; index avg `0.0241` n `26`; metal avg `-0.1652` n `20`; unknown avg `3.5867` n `820`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
