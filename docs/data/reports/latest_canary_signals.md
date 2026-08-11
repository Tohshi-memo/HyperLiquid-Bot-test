# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T04:22:25.018812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `0.0103` n `230`; crypto_major avg `0.0426` n `8`; equity avg `0.026` n `113`; fx avg `-0.0248` n `6`; index avg `-0.0003` n `25`; metal avg `-0.0317` n `20`; unknown avg `-0.0006` n `785`
- 1h: commodity avg `-0.0629` n `12`; crypto_alt avg `0.0224` n `230`; crypto_major avg `0.022` n `8`; equity avg `0.1654` n `113`; fx avg `-0.0215` n `6`; index avg `0.019` n `25`; metal avg `-0.0378` n `20`; unknown avg `1.3054` n `785`
- 4h: commodity avg `-0.0278` n `12`; crypto_alt avg `0.1166` n `230`; crypto_major avg `0.3588` n `8`; equity avg `0.6288` n `113`; fx avg `-0.0641` n `6`; index avg `0.1991` n `25`; metal avg `-0.0289` n `20`; unknown avg `-0.0192` n `785`
- 24h: commodity avg `0.7655` n `12`; crypto_alt avg `-0.5807` n `230`; crypto_major avg `-0.414` n `8`; equity avg `-0.8707` n `113`; fx avg `0.0977` n `6`; index avg `0.0597` n `25`; metal avg `0.4355` n `20`; unknown avg `103.9471` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1572`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.156`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1558`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.155`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.154`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1389`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1231`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1166`, n `669`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1072`, n `669`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0951`, n `669`, weak_sample_signal
