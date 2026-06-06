# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T01:52:24.380819+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0233` n `12`; crypto_alt avg `-0.4628` n `228`; crypto_major avg `-0.282` n `8`; equity avg `-0.4335` n `74`; fx avg `0.0014` n `6`; index avg `-0.266` n `23`; metal avg `-0.0608` n `18`; unknown avg `-0.2869` n `425`
- 1h: commodity avg `-0.0431` n `12`; crypto_alt avg `-0.8803` n `228`; crypto_major avg `-0.5373` n `8`; equity avg `-0.9378` n `74`; fx avg `-0.0216` n `6`; index avg `-0.409` n `23`; metal avg `-0.1122` n `18`; unknown avg `-0.2638` n `425`
- 4h: commodity avg `0.6896` n `12`; crypto_alt avg `-1.6566` n `228`; crypto_major avg `-1.1414` n `8`; equity avg `-1.3449` n `74`; fx avg `-0.0244` n `6`; index avg `-0.3887` n `23`; metal avg `-0.2777` n `18`; unknown avg `-0.0675` n `425`
- 24h: commodity avg `-1.1376` n `12`; crypto_alt avg `-6.4814` n `228`; crypto_major avg `-5.5799` n `8`; equity avg `-6.3873` n `74`; fx avg `-0.2337` n `6`; index avg `-3.9001` n `23`; metal avg `-3.809` n `18`; unknown avg `-1.4973` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
