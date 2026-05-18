# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T05:07:13.342435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0355` n `12`; crypto_alt avg `0.0861` n `228`; crypto_major avg `0.0227` n `8`; equity avg `0.1362` n `66`; fx avg `-0.0001` n `5`; index avg `0.0585` n `23`; metal avg `-0.0524` n `18`; unknown avg `-0.517` n `383`
- 1h: commodity avg `0.0321` n `12`; crypto_alt avg `0.3218` n `228`; crypto_major avg `0.2769` n `8`; equity avg `0.0347` n `66`; fx avg `0.0014` n `5`; index avg `0.0187` n `23`; metal avg `-0.154` n `18`; unknown avg `-0.7129` n `383`
- 4h: commodity avg `-0.014` n `12`; crypto_alt avg `0.3492` n `228`; crypto_major avg `-0.2021` n `8`; equity avg `0.554` n `66`; fx avg `0.043` n `5`; index avg `0.2218` n `23`; metal avg `0.8162` n `18`; unknown avg `-0.9304` n `383`
- 24h: commodity avg `2.6844` n `12`; crypto_alt avg `-10.6602` n `228`; crypto_major avg `-3.1745` n `8`; equity avg `-2.9425` n `65`; fx avg `-0.0624` n `5`; index avg `-1.7127` n `23`; metal avg `-6.1923` n `18`; unknown avg `550.0949` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
