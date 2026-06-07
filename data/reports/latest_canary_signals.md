# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T12:07:27.754052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `12`; crypto_alt avg `-0.124` n `228`; crypto_major avg `-0.0788` n `8`; equity avg `-0.0138` n `74`; fx avg `-0.0013` n `6`; index avg `-0.0057` n `23`; metal avg `-0.0156` n `18`; unknown avg `-0.027` n `516`
- 1h: commodity avg `0.0104` n `12`; crypto_alt avg `0.384` n `228`; crypto_major avg `0.2264` n `8`; equity avg `0.2602` n `74`; fx avg `-0.001` n `6`; index avg `0.1052` n `23`; metal avg `0.0039` n `18`; unknown avg `-0.041` n `516`
- 4h: commodity avg `0.0892` n `12`; crypto_alt avg `0.2678` n `228`; crypto_major avg `0.1891` n `8`; equity avg `0.0379` n `74`; fx avg `-0.0354` n `6`; index avg `-0.0707` n `23`; metal avg `-0.0218` n `18`; unknown avg `-4.7279` n `516`
- 24h: commodity avg `0.0628` n `12`; crypto_alt avg `2.818` n `228`; crypto_major avg `2.5558` n `8`; equity avg `1.893` n `74`; fx avg `0.0196` n `6`; index avg `0.6394` n `23`; metal avg `0.5257` n `18`; unknown avg `0.093` n `405`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
