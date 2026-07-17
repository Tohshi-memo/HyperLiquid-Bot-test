# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T10:07:32.315646+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `0.0992` n `230`; crypto_major avg `0.0713` n `8`; equity avg `0.2596` n `96`; fx avg `-0.019` n `6`; index avg `0.0312` n `25`; metal avg `-0.0081` n `20`; unknown avg `0.0144` n `769`
- 1h: commodity avg `0.093` n `12`; crypto_alt avg `0.3419` n `230`; crypto_major avg `0.3678` n `8`; equity avg `0.8963` n `96`; fx avg `-0.0134` n `6`; index avg `0.0937` n `25`; metal avg `0.0629` n `20`; unknown avg `0.0638` n `768`
- 4h: commodity avg `0.3554` n `12`; crypto_alt avg `0.3736` n `230`; crypto_major avg `0.4227` n `8`; equity avg `0.5397` n `96`; fx avg `0.0286` n `6`; index avg `0.0228` n `25`; metal avg `0.0691` n `20`; unknown avg `-0.0452` n `768`
- 24h: commodity avg `0.0273` n `12`; crypto_alt avg `-1.2701` n `230`; crypto_major avg `-2.5646` n `8`; equity avg `-4.758` n `94`; fx avg `-0.0282` n `6`; index avg `-0.6797` n `25`; metal avg `-0.6805` n `20`; unknown avg `-0.4159` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
