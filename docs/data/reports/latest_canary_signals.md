# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T05:37:16.863166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0104` n `12`; crypto_alt avg `0.4963` n `228`; crypto_major avg `0.3313` n `8`; equity avg `0.101` n `66`; fx avg `0.0064` n `6`; index avg `0.0353` n `23`; metal avg `0.0108` n `18`; unknown avg `0.6302` n `383`
- 1h: commodity avg `0.1538` n `12`; crypto_alt avg `0.057` n `228`; crypto_major avg `0.0263` n `8`; equity avg `-0.0241` n `66`; fx avg `0.0092` n `6`; index avg `0.1197` n `23`; metal avg `-0.0594` n `18`; unknown avg `-0.0726` n `383`
- 4h: commodity avg `0.1773` n `12`; crypto_alt avg `0.1316` n `228`; crypto_major avg `-0.1067` n `8`; equity avg `-0.2194` n `66`; fx avg `0.0539` n `6`; index avg `-0.1142` n `23`; metal avg `-0.7843` n `18`; unknown avg `-0.5108` n `383`
- 24h: commodity avg `0.3873` n `12`; crypto_alt avg `1.1031` n `228`; crypto_major avg `0.2397` n `8`; equity avg `-1.0029` n `66`; fx avg `0.287` n `6`; index avg `-0.4275` n `23`; metal avg `0.1616` n `18`; unknown avg `0.6801` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.2006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
