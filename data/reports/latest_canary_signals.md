# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T08:37:22.384115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `13`; crypto_alt avg `-0.2439` n `239`; crypto_major avg `-0.2219` n `8`; equity avg `0.026` n `162`; fx avg `0.1728` n `6`; index avg `-0.0026` n `27`; metal avg `-0.0002` n `20`; unknown avg `7.8561` n `1259`
- 1h: commodity avg `-0.0104` n `13`; crypto_alt avg `-0.2302` n `239`; crypto_major avg `-0.1812` n `8`; equity avg `0.0545` n `162`; fx avg `0.17` n `6`; index avg `0.0003` n `27`; metal avg `0.0011` n `20`; unknown avg `4.9709` n `1241`
- 4h: commodity avg `0.044` n `13`; crypto_alt avg `-0.8505` n `239`; crypto_major avg `-0.1466` n `8`; equity avg `0.1464` n `162`; fx avg `0.1694` n `6`; index avg `0.0118` n `27`; metal avg `0.022` n `20`; unknown avg `7.8446` n `1207`
- 24h: commodity avg `-0.1641` n `13`; crypto_alt avg `-2.8431` n `239`; crypto_major avg `-2.9597` n `8`; equity avg `-2.2996` n `162`; fx avg `0.003` n `6`; index avg `-0.1896` n `27`; metal avg `-0.3143` n `20`; unknown avg `63.8511` n `1057`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
