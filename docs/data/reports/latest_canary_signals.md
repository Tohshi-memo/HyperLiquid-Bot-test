# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T23:37:30.096668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0551` n `13`; crypto_alt avg `0.1004` n `235`; crypto_major avg `0.0068` n `8`; equity avg `0.0384` n `151`; fx avg `-0.0073` n `6`; index avg `0.0011` n `26`; metal avg `0.0021` n `20`; unknown avg `1.7713` n `1135`
- 1h: commodity avg `-0.0482` n `13`; crypto_alt avg `0.0089` n `235`; crypto_major avg `-0.1615` n `8`; equity avg `-0.1504` n `151`; fx avg `0.002` n `6`; index avg `-0.021` n `26`; metal avg `-0.0488` n `20`; unknown avg `0.2699` n `1133`
- 4h: commodity avg `-0.0067` n `13`; crypto_alt avg `0.0086` n `235`; crypto_major avg `-0.1825` n `8`; equity avg `0.1764` n `151`; fx avg `-0.0102` n `6`; index avg `-0.0138` n `26`; metal avg `-0.0849` n `20`; unknown avg `1.8776` n `1019`
- 24h: commodity avg `0.7584` n `13`; crypto_alt avg `1.0935` n `235`; crypto_major avg `1.3943` n `8`; equity avg `-0.1425` n `151`; fx avg `0.1651` n `6`; index avg `-0.1248` n `26`; metal avg `-0.3442` n `20`; unknown avg `0.3694` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1569`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1429`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1178`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0923`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0811`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
