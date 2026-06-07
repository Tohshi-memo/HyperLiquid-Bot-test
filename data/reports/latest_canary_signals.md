# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T11:37:23.751352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0084` n `12`; crypto_alt avg `0.4486` n `228`; crypto_major avg `0.3133` n `8`; equity avg `0.0729` n `74`; fx avg `-0.0038` n `6`; index avg `-0.0148` n `23`; metal avg `0.0145` n `18`; unknown avg `0.0212` n `516`
- 1h: commodity avg `0.0523` n `12`; crypto_alt avg `0.3145` n `228`; crypto_major avg `0.2806` n `8`; equity avg `0.2285` n `74`; fx avg `-0.0332` n `6`; index avg `0.0407` n `23`; metal avg `0.0071` n `18`; unknown avg `0.0559` n `516`
- 4h: commodity avg `-0.0821` n `12`; crypto_alt avg `0.2689` n `228`; crypto_major avg `0.267` n `8`; equity avg `-0.1013` n `74`; fx avg `-0.0392` n `6`; index avg `-0.2208` n `23`; metal avg `0.0043` n `18`; unknown avg `-4.7422` n `516`
- 24h: commodity avg `0.1042` n `12`; crypto_alt avg `3.2773` n `228`; crypto_major avg `3.0617` n `8`; equity avg `2.0077` n `74`; fx avg `0.0137` n `6`; index avg `0.6979` n `23`; metal avg `0.6211` n `18`; unknown avg `0.2576` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
