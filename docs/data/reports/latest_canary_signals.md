# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T23:37:15.738240+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1152` n `12`; crypto_alt avg `-0.2713` n `228`; crypto_major avg `-0.1873` n `8`; equity avg `-0.1154` n `66`; fx avg `-0.0031` n `5`; index avg `-0.1111` n `23`; metal avg `-0.0766` n `18`; unknown avg `-0.1937` n `383`
- 1h: commodity avg `0.2407` n `12`; crypto_alt avg `-0.711` n `228`; crypto_major avg `-0.6328` n `8`; equity avg `-0.4684` n `66`; fx avg `-0.004` n `5`; index avg `-0.2161` n `23`; metal avg `-0.1197` n `18`; unknown avg `-0.2505` n `383`
- 4h: commodity avg `0.1705` n `12`; crypto_alt avg `-1.0995` n `228`; crypto_major avg `-0.8133` n `8`; equity avg `0.0272` n `66`; fx avg `-0.0234` n `5`; index avg `-0.1063` n `23`; metal avg `0.4974` n `18`; unknown avg `-0.3575` n `383`
- 24h: commodity avg `2.0648` n `12`; crypto_alt avg `-10.2058` n `228`; crypto_major avg `-2.3006` n `8`; equity avg `-2.6932` n `65`; fx avg `-0.1778` n `5`; index avg `-1.6725` n `23`; metal avg `-5.4904` n `18`; unknown avg `550.2938` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
