# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T02:07:28.112968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0246` n `13`; crypto_alt avg `-0.0413` n `239`; crypto_major avg `-0.0821` n `8`; equity avg `0.0254` n `162`; fx avg `0.0015` n `6`; index avg `0.0005` n `27`; metal avg `-0.0301` n `20`; unknown avg `1.0328` n `1256`
- 1h: commodity avg `-0.0963` n `13`; crypto_alt avg `-0.1265` n `239`; crypto_major avg `-0.2106` n `8`; equity avg `0.2218` n `162`; fx avg `-0.0043` n `6`; index avg `0.0441` n `27`; metal avg `0.1997` n `20`; unknown avg `0.7111` n `1260`
- 4h: commodity avg `-0.1724` n `13`; crypto_alt avg `-0.0522` n `239`; crypto_major avg `-0.2631` n `8`; equity avg `0.827` n `162`; fx avg `-0.0199` n `6`; index avg `0.1335` n `27`; metal avg `0.2937` n `20`; unknown avg `0.3175` n `1217`
- 24h: commodity avg `0.7313` n `13`; crypto_alt avg `-0.7615` n `239`; crypto_major avg `-1.9338` n `8`; equity avg `-0.4944` n `162`; fx avg `-0.1098` n `6`; index avg `0.1067` n `27`; metal avg `-0.44` n `20`; unknown avg `52.2675` n `1119`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
