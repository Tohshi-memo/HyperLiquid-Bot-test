# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T23:52:37.929631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0532` n `13`; crypto_alt avg `0.0294` n `235`; crypto_major avg `-0.0246` n `8`; equity avg `-0.0374` n `151`; fx avg `-0.0065` n `6`; index avg `-0.0239` n `26`; metal avg `-0.0004` n `20`; unknown avg `1.7378` n `1135`
- 1h: commodity avg `-0.0024` n `13`; crypto_alt avg `-0.1043` n `235`; crypto_major avg `-0.2905` n `8`; equity avg `-0.2563` n `151`; fx avg `0.0061` n `6`; index avg `-0.0738` n `26`; metal avg `-0.0614` n `20`; unknown avg `1.2986` n `1133`
- 4h: commodity avg `0.0402` n `13`; crypto_alt avg `0.0338` n `235`; crypto_major avg `-0.1152` n `8`; equity avg `0.1979` n `151`; fx avg `-0.0151` n `6`; index avg `-0.0272` n `26`; metal avg `-0.0682` n `20`; unknown avg `1.3793` n `1019`
- 24h: commodity avg `0.8638` n `13`; crypto_alt avg `1.0448` n `235`; crypto_major avg `1.399` n `8`; equity avg `-0.0934` n `151`; fx avg `0.1566` n `6`; index avg `-0.1213` n `26`; metal avg `-0.3216` n `20`; unknown avg `0.0106` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1573`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1435`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1176`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0932`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0807`, n `666`, weak_sample_signal
