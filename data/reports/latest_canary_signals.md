# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T12:07:31.490076+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `13`; crypto_alt avg `0.3093` n `237`; crypto_major avg `0.2938` n `8`; equity avg `0.0644` n `151`; fx avg `0.0044` n `6`; index avg `0.007` n `26`; metal avg `0.0017` n `20`; unknown avg `0.2362` n `1185`
- 1h: commodity avg `0.059` n `13`; crypto_alt avg `0.1126` n `237`; crypto_major avg `0.1618` n `8`; equity avg `-0.0156` n `151`; fx avg `0.0111` n `6`; index avg `-0.0044` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.3244` n `1185`
- 4h: commodity avg `0.048` n `13`; crypto_alt avg `0.3971` n `237`; crypto_major avg `0.6536` n `8`; equity avg `0.2018` n `151`; fx avg `0.0021` n `6`; index avg `0.0311` n `26`; metal avg `0.0221` n `20`; unknown avg `5.3565` n `1089`
- 24h: commodity avg `0.0581` n `13`; crypto_alt avg `-1.8753` n `236`; crypto_major avg `0.0489` n `8`; equity avg `-0.5443` n `151`; fx avg `-0.0441` n `6`; index avg `-0.0548` n `26`; metal avg `-0.048` n `20`; unknown avg `5.1222` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2057`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1356`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1321`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1112`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0743`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
