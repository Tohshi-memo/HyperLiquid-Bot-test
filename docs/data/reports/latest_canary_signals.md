# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T01:07:30.050327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0787` n `12`; crypto_alt avg `-0.0752` n `233`; crypto_major avg `-0.0715` n `8`; equity avg `-0.1688` n `136`; fx avg `0.0166` n `6`; index avg `-0.018` n `27`; metal avg `-0.1239` n `20`; unknown avg `-0.2277` n `774`
- 1h: commodity avg `0.167` n `12`; crypto_alt avg `-0.0847` n `233`; crypto_major avg `-0.0501` n `8`; equity avg `-0.458` n `136`; fx avg `-0.0102` n `6`; index avg `0.0102` n `27`; metal avg `-0.1104` n `20`; unknown avg `12.0813` n `768`
- 4h: commodity avg `0.4178` n `12`; crypto_alt avg `-1.5958` n `233`; crypto_major avg `-1.0915` n `8`; equity avg `-0.8367` n `136`; fx avg `0.0126` n `6`; index avg `-0.1737` n `27`; metal avg `-0.1373` n `20`; unknown avg `1.1724` n `768`
- 24h: commodity avg `0.7749` n `12`; crypto_alt avg `-1.7014` n `233`; crypto_major avg `-1.5389` n `8`; equity avg `-1.909` n `136`; fx avg `0.0612` n `6`; index avg `-0.3944` n `26`; metal avg `-0.1869` n `20`; unknown avg `1.3944` n `682`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
