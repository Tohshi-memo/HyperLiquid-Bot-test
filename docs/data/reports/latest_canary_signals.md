# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T17:22:26.878867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0496` n `12`; crypto_alt avg `0.185` n `230`; crypto_major avg `0.1653` n `8`; equity avg `0.0801` n `114`; fx avg `-0.0064` n `6`; index avg `0.0088` n `25`; metal avg `0.0137` n `20`; unknown avg `0.0224` n `791`
- 1h: commodity avg `0.072` n `12`; crypto_alt avg `0.2372` n `230`; crypto_major avg `0.1203` n `8`; equity avg `0.0239` n `114`; fx avg `-0.0246` n `6`; index avg `-0.001` n `25`; metal avg `-0.035` n `20`; unknown avg `18.6884` n `791`
- 4h: commodity avg `0.2158` n `12`; crypto_alt avg `0.7763` n `230`; crypto_major avg `0.47` n `8`; equity avg `-0.5971` n `114`; fx avg `0.0858` n `6`; index avg `-0.1394` n `25`; metal avg `0.0653` n `20`; unknown avg `0.1407` n `786`
- 24h: commodity avg `0.0876` n `12`; crypto_alt avg `0.6324` n `230`; crypto_major avg `-0.3427` n `8`; equity avg `-0.6517` n `114`; fx avg `0.0709` n `6`; index avg `-0.1398` n `25`; metal avg `0.1271` n `20`; unknown avg `-0.0018` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1905`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
