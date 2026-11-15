# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T17:52:26.910300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5161` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5146` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0054` n `13`; crypto_alt avg `0.1989` n `239`; crypto_major avg `0.2621` n `8`; equity avg `-0.0101` n `162`; fx avg `-0.0037` n `6`; index avg `0.0042` n `27`; metal avg `0.0156` n `20`; unknown avg `1.1015` n `1265`
- 1h: commodity avg `-0.0233` n `13`; crypto_alt avg `-0.0383` n `239`; crypto_major avg `0.042` n `8`; equity avg `-0.1693` n `162`; fx avg `-0.0029` n `6`; index avg `-0.0249` n `27`; metal avg `0.0301` n `20`; unknown avg `1.4844` n `1263`
- 4h: commodity avg `-0.0174` n `13`; crypto_alt avg `-1.4944` n `239`; crypto_major avg `-1.5095` n `8`; equity avg `-0.1149` n `162`; fx avg `-0.0013` n `6`; index avg `0.0051` n `27`; metal avg `0.0066` n `20`; unknown avg `1.0805` n `1256`
- 24h: commodity avg `0.0255` n `13`; crypto_alt avg `-1.6505` n `239`; crypto_major avg `-1.0302` n `8`; equity avg `0.0932` n `162`; fx avg `-0.0159` n `6`; index avg `0.0284` n `27`; metal avg `-0.1344` n `20`; unknown avg `0.3291` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
