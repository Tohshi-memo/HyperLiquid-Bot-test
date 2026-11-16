# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T19:07:28.149730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `13`; crypto_alt avg `-0.3093` n `239`; crypto_major avg `-0.3102` n `8`; equity avg `-0.0937` n `162`; fx avg `0.0116` n `6`; index avg `-0.0288` n `27`; metal avg `0.0066` n `20`; unknown avg `0.5989` n `1260`
- 1h: commodity avg `-0.1324` n `13`; crypto_alt avg `0.1788` n `239`; crypto_major avg `0.1211` n `8`; equity avg `0.0321` n `162`; fx avg `-0.0056` n `6`; index avg `-0.0225` n `27`; metal avg `0.03` n `20`; unknown avg `13.2677` n `1262`
- 4h: commodity avg `-0.3155` n `13`; crypto_alt avg `0.4833` n `239`; crypto_major avg `0.5016` n `8`; equity avg `-0.2679` n `162`; fx avg `-0.0319` n `6`; index avg `-0.0304` n `27`; metal avg `-0.1459` n `20`; unknown avg `8.22` n `1239`
- 24h: commodity avg `-1.1294` n `13`; crypto_alt avg `0.1647` n `239`; crypto_major avg `0.2317` n `8`; equity avg `-2.6915` n `162`; fx avg `-0.0943` n `6`; index avg `-0.2523` n `27`; metal avg `-0.2689` n `20`; unknown avg `251.0053` n `1037`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1345`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1266`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1191`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1089`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.103`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1014`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0935`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0884`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.086`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `669`, weak_sample_signal
