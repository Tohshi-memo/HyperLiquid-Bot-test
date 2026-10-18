# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T05:22:33.079517+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `13`; crypto_alt avg `-0.0982` n `237`; crypto_major avg `-0.022` n `8`; equity avg `-0.0786` n `151`; fx avg `0.0025` n `6`; index avg `-0.0096` n `26`; metal avg `0.0017` n `20`; unknown avg `0.0104` n `1193`
- 1h: commodity avg `-0.033` n `13`; crypto_alt avg `-0.4999` n `237`; crypto_major avg `-0.2553` n `8`; equity avg `0.0248` n `151`; fx avg `0.0053` n `6`; index avg `0.0099` n `26`; metal avg `0.0014` n `20`; unknown avg `-0.0223` n `1191`
- 4h: commodity avg `0.0101` n `13`; crypto_alt avg `-0.5829` n `237`; crypto_major avg `0.1049` n `8`; equity avg `0.0581` n `151`; fx avg `-0.0156` n `6`; index avg `0.0269` n `26`; metal avg `0.0115` n `20`; unknown avg `3.5031` n `1185`
- 24h: commodity avg `-0.1557` n `13`; crypto_alt avg `-2.8445` n `236`; crypto_major avg `-0.7225` n `8`; equity avg `-0.9018` n `151`; fx avg `-0.0409` n `6`; index avg `-0.1008` n `26`; metal avg `-0.0525` n `20`; unknown avg `2.8737` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1694`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.133`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1064`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.106`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0797`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
