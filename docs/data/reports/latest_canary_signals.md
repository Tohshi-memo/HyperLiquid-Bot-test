# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T04:07:14.529838+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `12`; crypto_alt avg `0.0257` n `228`; crypto_major avg `-0.055` n `8`; equity avg `-0.2171` n `66`; fx avg `0.005` n `6`; index avg `-0.1854` n `23`; metal avg `-0.197` n `18`; unknown avg `-0.0607` n `383`
- 1h: commodity avg `-0.0513` n `12`; crypto_alt avg `0.4229` n `228`; crypto_major avg `0.3591` n `8`; equity avg `0.0314` n `66`; fx avg `0.018` n `6`; index avg `-0.0965` n `23`; metal avg `-0.2494` n `18`; unknown avg `-0.1364` n `383`
- 4h: commodity avg `0.0841` n `12`; crypto_alt avg `0.0` n `228`; crypto_major avg `-0.1981` n `8`; equity avg `-0.5538` n `66`; fx avg `0.1013` n `6`; index avg `-0.4509` n `23`; metal avg `-1.4631` n `18`; unknown avg `-0.6887` n `383`
- 24h: commodity avg `0.2169` n `12`; crypto_alt avg `1.0393` n `228`; crypto_major avg `0.4633` n `8`; equity avg `-0.9451` n `66`; fx avg `0.2512` n `6`; index avg `-0.4812` n `23`; metal avg `0.1979` n `18`; unknown avg `0.5213` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
