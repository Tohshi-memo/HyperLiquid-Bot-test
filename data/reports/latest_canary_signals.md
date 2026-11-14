# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T01:37:26.478127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0158` n `13`; crypto_alt avg `-0.0977` n `239`; crypto_major avg `-0.007` n `8`; equity avg `0.0129` n `162`; fx avg `0.0022` n `6`; index avg `0.0001` n `27`; metal avg `0.0204` n `20`; unknown avg `-0.0005` n `1262`
- 1h: commodity avg `0.0358` n `13`; crypto_alt avg `-0.0571` n `239`; crypto_major avg `-0.1628` n `8`; equity avg `0.0016` n `162`; fx avg `-0.0045` n `6`; index avg `-0.0189` n `27`; metal avg `0.0243` n `20`; unknown avg `0.0539` n `1260`
- 4h: commodity avg `-0.0248` n `13`; crypto_alt avg `-0.4265` n `239`; crypto_major avg `-0.5506` n `8`; equity avg `-0.2705` n `162`; fx avg `-0.0179` n `6`; index avg `0.0032` n `27`; metal avg `0.0921` n `20`; unknown avg `0.7178` n `1200`
- 24h: commodity avg `-0.098` n `13`; crypto_alt avg `-1.717` n `239`; crypto_major avg `-3.0` n `8`; equity avg `-4.0933` n `162`; fx avg `-0.0606` n `6`; index avg `-0.3809` n `27`; metal avg `-0.5745` n `20`; unknown avg `60.1586` n `1036`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
