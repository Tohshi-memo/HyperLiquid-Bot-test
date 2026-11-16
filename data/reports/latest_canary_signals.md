# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T15:52:26.472346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0524` n `13`; crypto_alt avg `0.7764` n `239`; crypto_major avg `0.8346` n `8`; equity avg `0.8606` n `162`; fx avg `-0.0073` n `6`; index avg `0.1029` n `27`; metal avg `0.0398` n `20`; unknown avg `0.8344` n `1257`
- 1h: commodity avg `0.0467` n `13`; crypto_alt avg `-0.8372` n `239`; crypto_major avg `-0.9909` n `8`; equity avg `-0.528` n `162`; fx avg `-0.0267` n `6`; index avg `-0.0046` n `27`; metal avg `-0.2092` n `20`; unknown avg `0.5088` n `1241`
- 4h: commodity avg `-0.273` n `13`; crypto_alt avg `-0.0048` n `239`; crypto_major avg `-0.0813` n `8`; equity avg `-1.0646` n `162`; fx avg `-0.0029` n `6`; index avg `-0.0524` n `27`; metal avg `-0.2835` n `20`; unknown avg `29.4061` n `1227`
- 24h: commodity avg `-0.6836` n `13`; crypto_alt avg `0.0583` n `239`; crypto_major avg `0.0541` n `8`; equity avg `-1.8313` n `162`; fx avg `-0.0387` n `6`; index avg `-0.1306` n `27`; metal avg `-0.1227` n `20`; unknown avg `256.4999` n `1032`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
