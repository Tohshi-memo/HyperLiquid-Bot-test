# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T21:37:18.815474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0286` n `12`; crypto_alt avg `0.3313` n `228`; crypto_major avg `0.313` n `8`; equity avg `0.0733` n `66`; fx avg `-0.0044` n `6`; index avg `0.1372` n `23`; metal avg `0.0298` n `18`; unknown avg `-0.0147` n `383`
- 1h: commodity avg `0.2391` n `12`; crypto_alt avg `0.3682` n `228`; crypto_major avg `0.6062` n `8`; equity avg `0.1794` n `66`; fx avg `-0.035` n `6`; index avg `0.227` n `23`; metal avg `0.1596` n `18`; unknown avg `0.3581` n `383`
- 4h: commodity avg `-0.2397` n `12`; crypto_alt avg `1.2983` n `228`; crypto_major avg `1.3305` n `8`; equity avg `0.5661` n `66`; fx avg `-0.0639` n `6`; index avg `0.4447` n `23`; metal avg `0.4264` n `18`; unknown avg `0.7684` n `383`
- 24h: commodity avg `1.0099` n `12`; crypto_alt avg `-1.6701` n `228`; crypto_major avg `-1.7401` n `8`; equity avg `-0.816` n `66`; fx avg `0.1721` n `6`; index avg `-0.2459` n `23`; metal avg `1.1291` n `18`; unknown avg `0.0185` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
