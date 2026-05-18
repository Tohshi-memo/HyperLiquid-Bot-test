# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T21:42:24.855562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0366` n `12`; crypto_alt avg `0.3416` n `228`; crypto_major avg `0.3332` n `8`; equity avg `0.1147` n `66`; fx avg `-0.0051` n `6`; index avg `0.1189` n `23`; metal avg `-0.0019` n `18`; unknown avg `-0.0533` n `383`
- 1h: commodity avg `0.174` n `12`; crypto_alt avg `0.3784` n `228`; crypto_major avg `0.6255` n `8`; equity avg `0.2242` n `66`; fx avg `-0.0358` n `6`; index avg `0.2089` n `23`; metal avg `0.1278` n `18`; unknown avg `0.3276` n `383`
- 4h: commodity avg `-0.304` n `12`; crypto_alt avg `1.3087` n `228`; crypto_major avg `1.3499` n `8`; equity avg `0.6115` n `66`; fx avg `-0.0646` n `6`; index avg `0.4265` n `23`; metal avg `0.3945` n `18`; unknown avg `0.7115` n `383`
- 24h: commodity avg `0.9451` n `12`; crypto_alt avg `-1.6594` n `228`; crypto_major avg `-1.7221` n `8`; equity avg `-0.7724` n `66`; fx avg `0.1713` n `6`; index avg `-0.2643` n `23`; metal avg `1.0971` n `18`; unknown avg `0.0048` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
