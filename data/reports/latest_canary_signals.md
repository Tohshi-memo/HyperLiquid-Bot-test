# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T19:52:19.691390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0443` n `12`; crypto_alt avg `0.2364` n `228`; crypto_major avg `0.2975` n `8`; equity avg `0.0942` n `65`; fx avg `0.0` n `5`; index avg `0.019` n `23`; metal avg `-0.0086` n `18`; unknown avg `0.1161` n `384`
- 1h: commodity avg `-0.0295` n `12`; crypto_alt avg `0.5963` n `228`; crypto_major avg `0.9687` n `8`; equity avg `0.2276` n `65`; fx avg `-0.0011` n `5`; index avg `0.0467` n `23`; metal avg `-0.0624` n `18`; unknown avg `1.0954` n `384`
- 4h: commodity avg `0.0257` n `12`; crypto_alt avg `0.2969` n `228`; crypto_major avg `1.2951` n `8`; equity avg `0.2485` n `65`; fx avg `0.0101` n `5`; index avg `0.0462` n `23`; metal avg `-0.1324` n `18`; unknown avg `1.1915` n `384`
- 24h: commodity avg `1.8311` n `12`; crypto_alt avg `-9.0389` n `228`; crypto_major avg `-1.1847` n `8`; equity avg `-2.3269` n `65`; fx avg `-0.1549` n `5`; index avg `-1.549` n `23`; metal avg `-5.9545` n `18`; unknown avg `551.1923` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
