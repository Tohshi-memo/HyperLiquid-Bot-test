# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T10:07:30.129428+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0647` n `12`; crypto_alt avg `-0.0661` n `233`; crypto_major avg `-0.0605` n `8`; equity avg `-0.001` n `136`; fx avg `0.0162` n `6`; index avg `0.004` n `27`; metal avg `0.0216` n `20`; unknown avg `0.7387` n `892`
- 1h: commodity avg `-0.1175` n `12`; crypto_alt avg `0.2794` n `233`; crypto_major avg `0.4689` n `8`; equity avg `-0.0311` n `136`; fx avg `0.0117` n `6`; index avg `-0.0286` n `27`; metal avg `-0.1907` n `20`; unknown avg `5.2009` n `892`
- 4h: commodity avg `0.0789` n `12`; crypto_alt avg `-0.3497` n `233`; crypto_major avg `0.1713` n `8`; equity avg `-0.7361` n `136`; fx avg `0.0097` n `6`; index avg `-0.1534` n `27`; metal avg `-0.4548` n `20`; unknown avg `5.1652` n `858`
- 24h: commodity avg `0.5938` n `12`; crypto_alt avg `0.3297` n `233`; crypto_major avg `1.91` n `8`; equity avg `-1.0661` n `136`; fx avg `0.0338` n `6`; index avg `-0.2882` n `27`; metal avg `-0.5355` n `20`; unknown avg `1.0324` n `650`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
