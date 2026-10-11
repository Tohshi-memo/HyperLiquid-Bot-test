# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T19:37:26.408073+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0116` n `13`; crypto_alt avg `0.0123` n `235`; crypto_major avg `-0.0271` n `8`; equity avg `0.0128` n `150`; fx avg `0.0017` n `6`; index avg `0.0053` n `26`; metal avg `0.0019` n `20`; unknown avg `6.0563` n `1134`
- 1h: commodity avg `0.0313` n `13`; crypto_alt avg `0.0578` n `235`; crypto_major avg `-0.1773` n `8`; equity avg `-0.0125` n `150`; fx avg `-0.0025` n `6`; index avg `-0.0007` n `26`; metal avg `0.0041` n `20`; unknown avg `-0.34` n `1130`
- 4h: commodity avg `0.0718` n `13`; crypto_alt avg `0.6814` n `235`; crypto_major avg `0.5557` n `8`; equity avg `0.1784` n `150`; fx avg `0.0041` n `6`; index avg `0.0354` n `26`; metal avg `0.0433` n `20`; unknown avg `0.04` n `1092`
- 24h: commodity avg `0.2893` n `13`; crypto_alt avg `1.8523` n `235`; crypto_major avg `0.5883` n `8`; equity avg `0.2806` n `150`; fx avg `0.0211` n `6`; index avg `0.0461` n `26`; metal avg `0.0761` n `20`; unknown avg `0.8326` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
