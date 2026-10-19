# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T19:52:33.881639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `13`; crypto_alt avg `-0.1619` n `237`; crypto_major avg `-0.202` n `8`; equity avg `-0.4105` n `151`; fx avg `-0.0022` n `6`; index avg `-0.0723` n `26`; metal avg `-0.0223` n `20`; unknown avg `51.1523` n `1196`
- 1h: commodity avg `0.0335` n `13`; crypto_alt avg `-0.1597` n `237`; crypto_major avg `-0.254` n `8`; equity avg `-0.003` n `151`; fx avg `0.0003` n `6`; index avg `-0.0225` n `26`; metal avg `-0.0563` n `20`; unknown avg `7.677` n `1194`
- 4h: commodity avg `0.0123` n `13`; crypto_alt avg `-0.2435` n `237`; crypto_major avg `-0.2907` n `8`; equity avg `-1.1146` n `151`; fx avg `0.0044` n `6`; index avg `-0.1922` n `26`; metal avg `-0.034` n `20`; unknown avg `9.5994` n `1188`
- 24h: commodity avg `-0.263` n `13`; crypto_alt avg `2.8952` n `237`; crypto_major avg `2.1265` n `8`; equity avg `2.9153` n `151`; fx avg `-0.0128` n `6`; index avg `0.5649` n `26`; metal avg `0.1114` n `20`; unknown avg `13.7039` n `920`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.194`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
