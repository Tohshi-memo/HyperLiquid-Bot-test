# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T04:07:32.554737+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `13`; crypto_alt avg `0.0446` n `235`; crypto_major avg `0.0951` n `8`; equity avg `0.1206` n `150`; fx avg `0.0006` n `6`; index avg `0.0137` n `26`; metal avg `0.0117` n `20`; unknown avg `-0.021` n `1070`
- 1h: commodity avg `-0.0485` n `13`; crypto_alt avg `0.4603` n `235`; crypto_major avg `0.2748` n `8`; equity avg `0.3045` n `150`; fx avg `0.0055` n `6`; index avg `0.0324` n `26`; metal avg `0.0445` n `20`; unknown avg `1.1938` n `1070`
- 4h: commodity avg `-0.2621` n `13`; crypto_alt avg `1.2909` n `235`; crypto_major avg `0.7996` n `8`; equity avg `0.5694` n `150`; fx avg `0.0079` n `6`; index avg `0.0969` n `26`; metal avg `0.3136` n `20`; unknown avg `1.6267` n `1070`
- 24h: commodity avg `0.1181` n `13`; crypto_alt avg `-1.7386` n `235`; crypto_major avg `-2.4378` n `8`; equity avg `-1.6281` n `150`; fx avg `0.1175` n `6`; index avg `-0.1383` n `26`; metal avg `0.1109` n `20`; unknown avg `6.1117` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
