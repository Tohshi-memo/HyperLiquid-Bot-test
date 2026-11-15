# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T21:07:27.926395+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0277` n `13`; crypto_alt avg `0.0023` n `239`; crypto_major avg `-0.0734` n `8`; equity avg `0.0329` n `162`; fx avg `0.0131` n `6`; index avg `0.0126` n `27`; metal avg `-0.011` n `20`; unknown avg `15.4354` n `1243`
- 1h: commodity avg `-0.0435` n `13`; crypto_alt avg `0.458` n `239`; crypto_major avg `0.398` n `8`; equity avg `0.196` n `162`; fx avg `0.0159` n `6`; index avg `0.0319` n `27`; metal avg `0.0341` n `20`; unknown avg `14.9367` n `1247`
- 4h: commodity avg `0.0189` n `13`; crypto_alt avg `0.7401` n `239`; crypto_major avg `0.7028` n `8`; equity avg `0.374` n `162`; fx avg `0.0712` n `6`; index avg `0.0532` n `27`; metal avg `0.1098` n `20`; unknown avg `20.6331` n `1235`
- 24h: commodity avg `0.0694` n `13`; crypto_alt avg `2.8117` n `239`; crypto_major avg `2.5736` n `8`; equity avg `1.4483` n `162`; fx avg `0.0559` n `6`; index avg `0.1426` n `27`; metal avg `0.3881` n `20`; unknown avg `243.4862` n `1154`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
