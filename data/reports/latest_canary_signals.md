# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T03:52:16.004656+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0444` n `12`; crypto_alt avg `0.0619` n `228`; crypto_major avg `0.0949` n `8`; equity avg `-0.0806` n `66`; fx avg `0.0107` n `6`; index avg `-0.0492` n `23`; metal avg `-0.0086` n `18`; unknown avg `-0.0005` n `383`
- 1h: commodity avg `-0.024` n `12`; crypto_alt avg `0.385` n `228`; crypto_major avg `0.3363` n `8`; equity avg `0.241` n `66`; fx avg `0.0356` n `6`; index avg `0.1198` n `23`; metal avg `-0.0098` n `18`; unknown avg `-0.0272` n `383`
- 4h: commodity avg `0.2247` n `12`; crypto_alt avg `0.0963` n `228`; crypto_major avg `0.0332` n `8`; equity avg `-0.4082` n `66`; fx avg `0.1372` n `6`; index avg `-0.2791` n `23`; metal avg `-1.3028` n `18`; unknown avg `-0.6073` n `383`
- 24h: commodity avg `0.1805` n `12`; crypto_alt avg `1.1243` n `228`; crypto_major avg `0.5317` n `8`; equity avg `-0.6661` n `66`; fx avg `0.2507` n `6`; index avg `-0.2493` n `23`; metal avg `0.6664` n `18`; unknown avg `0.5739` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
