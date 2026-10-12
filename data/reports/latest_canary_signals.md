# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T04:52:33.412593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0255` n `13`; crypto_alt avg `0.0517` n `235`; crypto_major avg `0.1982` n `8`; equity avg `0.0286` n `151`; fx avg `0.0164` n `6`; index avg `-0.0048` n `26`; metal avg `-0.0185` n `20`; unknown avg `0.5208` n `1105`
- 1h: commodity avg `0.0374` n `13`; crypto_alt avg `0.5727` n `235`; crypto_major avg `0.6769` n `8`; equity avg `0.1089` n `151`; fx avg `0.0248` n `6`; index avg `0.0094` n `26`; metal avg `-0.0433` n `20`; unknown avg `-0.0535` n `1071`
- 4h: commodity avg `-0.0591` n `13`; crypto_alt avg `0.7613` n `235`; crypto_major avg `0.6331` n `8`; equity avg `-0.5416` n `151`; fx avg `-0.0054` n `6`; index avg `-0.0036` n `26`; metal avg `-0.0357` n `20`; unknown avg `0.2177` n `1051`
- 24h: commodity avg `-0.4342` n `13`; crypto_alt avg `3.2486` n `235`; crypto_major avg `1.8083` n `8`; equity avg `-0.1281` n `151`; fx avg `-0.0501` n `6`; index avg `0.0236` n `26`; metal avg `0.1246` n `20`; unknown avg `1.1354` n `874`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
