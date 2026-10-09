# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T07:22:26.953317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0132` n `13`; crypto_alt avg `0.2145` n `235`; crypto_major avg `0.1477` n `8`; equity avg `0.032` n `150`; fx avg `0.0151` n `6`; index avg `0.0087` n `26`; metal avg `0.0301` n `20`; unknown avg `0.0069` n `1078`
- 1h: commodity avg `0.0317` n `13`; crypto_alt avg `0.2246` n `235`; crypto_major avg `0.1358` n `8`; equity avg `0.1758` n `150`; fx avg `0.0034` n `6`; index avg `0.0327` n `26`; metal avg `0.0793` n `20`; unknown avg `1.8244` n `1076`
- 4h: commodity avg `0.03` n `13`; crypto_alt avg `0.7486` n `235`; crypto_major avg `0.4276` n `8`; equity avg `0.8152` n `150`; fx avg `0.0295` n `6`; index avg `0.0963` n `26`; metal avg `0.1782` n `20`; unknown avg `7.2421` n `1040`
- 24h: commodity avg `-0.1661` n `13`; crypto_alt avg `-1.3403` n `235`; crypto_major avg `-2.1672` n `8`; equity avg `-0.5363` n `150`; fx avg `0.1361` n `6`; index avg `0.0274` n `26`; metal avg `0.4519` n `20`; unknown avg `6.5771` n `989`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
