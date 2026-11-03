# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T02:37:29.395721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0412` n `13`; crypto_alt avg `0.1673` n `239`; crypto_major avg `0.0881` n `8`; equity avg `0.0158` n `157`; fx avg `-0.0021` n `6`; index avg `-0.0001` n `27`; metal avg `-0.0345` n `20`; unknown avg `0.5357` n `1262`
- 1h: commodity avg `0.0571` n `13`; crypto_alt avg `-0.1018` n `239`; crypto_major avg `-0.0374` n `8`; equity avg `0.1295` n `157`; fx avg `-0.0427` n `6`; index avg `0.0022` n `27`; metal avg `-0.059` n `20`; unknown avg `0.2124` n `1258`
- 4h: commodity avg `0.1029` n `13`; crypto_alt avg `-0.1224` n `239`; crypto_major avg `0.3251` n `8`; equity avg `0.7455` n `157`; fx avg `-0.0793` n `6`; index avg `0.1141` n `27`; metal avg `-0.1118` n `20`; unknown avg `-0.1407` n `1246`
- 24h: commodity avg `-1.0018` n `13`; crypto_alt avg `-2.9859` n `238`; crypto_major avg `-1.698` n `8`; equity avg `-3.048` n `157`; fx avg `0.0094` n `6`; index avg `-0.1515` n `27`; metal avg `0.0619` n `20`; unknown avg `12.3414` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1676`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
