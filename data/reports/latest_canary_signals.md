# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T12:37:25.682435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `13`; crypto_alt avg `-0.0113` n `237`; crypto_major avg `-0.1155` n `8`; equity avg `-0.0371` n `151`; fx avg `0.0014` n `6`; index avg `-0.0115` n `26`; metal avg `-0.007` n `20`; unknown avg `0.0556` n `1193`
- 1h: commodity avg `-0.0092` n `13`; crypto_alt avg `0.2069` n `237`; crypto_major avg `-0.0301` n `8`; equity avg `0.0287` n `151`; fx avg `0.004` n `6`; index avg `-0.0054` n `26`; metal avg `-0.0064` n `20`; unknown avg `0.0958` n `1185`
- 4h: commodity avg `0.0207` n `13`; crypto_alt avg `0.5414` n `237`; crypto_major avg `0.4596` n `8`; equity avg `0.1706` n `151`; fx avg `0.0108` n `6`; index avg `0.0183` n `26`; metal avg `0.02` n `20`; unknown avg `5.4497` n `1089`
- 24h: commodity avg `0.0599` n `13`; crypto_alt avg `-1.9642` n `236`; crypto_major avg `-0.087` n `8`; equity avg `-0.5045` n `151`; fx avg `-0.0427` n `6`; index avg `-0.0537` n `26`; metal avg `-0.0433` n `20`; unknown avg `1.7363` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2067`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1368`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1328`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1116`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0743`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
