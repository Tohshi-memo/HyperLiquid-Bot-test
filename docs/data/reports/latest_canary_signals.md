# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T15:22:31.151844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `13`; crypto_alt avg `0.0116` n `235`; crypto_major avg `0.0269` n `8`; equity avg `0.0034` n `150`; fx avg `-0.0019` n `6`; index avg `0.003` n `26`; metal avg `0.0041` n `20`; unknown avg `4.2623` n `1134`
- 1h: commodity avg `0.1116` n `13`; crypto_alt avg `0.5812` n `235`; crypto_major avg `0.2972` n `8`; equity avg `0.0212` n `150`; fx avg `0.0065` n `6`; index avg `0.0019` n `26`; metal avg `-0.0029` n `20`; unknown avg `0.1088` n `1132`
- 4h: commodity avg `-0.1228` n `13`; crypto_alt avg `1.1317` n `235`; crypto_major avg `0.3877` n `8`; equity avg `0.1068` n `150`; fx avg `-0.0019` n `6`; index avg `0.0086` n `26`; metal avg `0.013` n `20`; unknown avg `5.0039` n `1053`
- 24h: commodity avg `0.2199` n `13`; crypto_alt avg `1.2775` n `235`; crypto_major avg `-0.22` n `8`; equity avg `0.0696` n `150`; fx avg `0.0151` n `6`; index avg `-0.0093` n `26`; metal avg `0.0088` n `20`; unknown avg `1.3208` n `941`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
