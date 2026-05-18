# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T19:37:16.117521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0125` n `12`; crypto_alt avg `0.3581` n `228`; crypto_major avg `0.1674` n `8`; equity avg `0.1538` n `66`; fx avg `-0.012` n `6`; index avg `0.1022` n `23`; metal avg `0.0057` n `18`; unknown avg `0.0358` n `383`
- 1h: commodity avg `-0.6989` n `12`; crypto_alt avg `1.0828` n `228`; crypto_major avg `0.6691` n `8`; equity avg `0.4873` n `66`; fx avg `0.0239` n `6`; index avg `0.2264` n `23`; metal avg `0.3856` n `18`; unknown avg `0.3595` n `383`
- 4h: commodity avg `-0.0309` n `12`; crypto_alt avg `1.0194` n `228`; crypto_major avg `0.6136` n `8`; equity avg `-0.3648` n `66`; fx avg `-0.0328` n `6`; index avg `-0.1251` n `23`; metal avg `0.288` n `18`; unknown avg `0.0079` n `383`
- 24h: commodity avg `0.6711` n `12`; crypto_alt avg `-2.074` n `228`; crypto_major avg `-2.4335` n `8`; equity avg `-1.1879` n `66`; fx avg `0.1595` n `6`; index avg `-0.5387` n `23`; metal avg `0.811` n `18`; unknown avg `-0.5129` n `362`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1648`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
