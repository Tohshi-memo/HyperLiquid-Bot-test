# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T10:37:17.363962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0338` n `12`; crypto_alt avg `0.1802` n `228`; crypto_major avg `0.3153` n `8`; equity avg `0.1772` n `66`; fx avg `-0.0146` n `6`; index avg `0.0412` n `23`; metal avg `0.1289` n `18`; unknown avg `0.2283` n `383`
- 1h: commodity avg `-0.144` n `12`; crypto_alt avg `0.1524` n `228`; crypto_major avg `0.3475` n `8`; equity avg `0.1603` n `66`; fx avg `0.0276` n `6`; index avg `-0.0023` n `23`; metal avg `0.149` n `18`; unknown avg `-0.1718` n `383`
- 4h: commodity avg `-0.103` n `12`; crypto_alt avg `-0.6314` n `228`; crypto_major avg `-0.0932` n `8`; equity avg `-0.3216` n `66`; fx avg `-0.0562` n `6`; index avg `-0.3077` n `23`; metal avg `-0.2557` n `18`; unknown avg `-0.2626` n `383`
- 24h: commodity avg `0.3954` n `12`; crypto_alt avg `1.6267` n `228`; crypto_major avg `0.9697` n `8`; equity avg `-1.3835` n `66`; fx avg `0.2235` n `6`; index avg `-0.7127` n `23`; metal avg `0.0585` n `18`; unknown avg `0.9218` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
