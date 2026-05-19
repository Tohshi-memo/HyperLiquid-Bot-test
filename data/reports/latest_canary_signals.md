# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T12:52:17.290096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0148` n `12`; crypto_alt avg `0.073` n `228`; crypto_major avg `0.2295` n `8`; equity avg `0.0276` n `66`; fx avg `-0.0204` n `6`; index avg `0.0034` n `23`; metal avg `-0.0357` n `18`; unknown avg `0.4163` n `383`
- 1h: commodity avg `-0.2323` n `12`; crypto_alt avg `0.2443` n `228`; crypto_major avg `0.2954` n `8`; equity avg `0.1116` n `66`; fx avg `-0.0176` n `6`; index avg `0.0676` n `23`; metal avg `-0.027` n `18`; unknown avg `-0.0138` n `383`
- 4h: commodity avg `0.2202` n `12`; crypto_alt avg `-0.8051` n `228`; crypto_major avg `-0.3929` n `8`; equity avg `-0.6329` n `66`; fx avg `-0.072` n `6`; index avg `-0.2829` n `23`; metal avg `-0.1414` n `18`; unknown avg `-0.6902` n `383`
- 24h: commodity avg `1.6732` n `12`; crypto_alt avg `-0.0805` n `228`; crypto_major avg `-0.2198` n `8`; equity avg `-2.4543` n `66`; fx avg `0.2161` n `6`; index avg `-1.2669` n `23`; metal avg `-0.9266` n `18`; unknown avg `0.3342` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
