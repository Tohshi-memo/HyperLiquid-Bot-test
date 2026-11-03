# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T12:07:25.913110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `13`; crypto_alt avg `-0.184` n `239`; crypto_major avg `0.0204` n `8`; equity avg `-0.0658` n `157`; fx avg `0.0131` n `6`; index avg `-0.0086` n `27`; metal avg `-0.039` n `20`; unknown avg `0.3178` n `1252`
- 1h: commodity avg `0.1157` n `13`; crypto_alt avg `0.1291` n `239`; crypto_major avg `-0.1344` n `8`; equity avg `-0.3777` n `157`; fx avg `0.0192` n `6`; index avg `-0.0461` n `27`; metal avg `-0.0339` n `20`; unknown avg `1.4647` n `1244`
- 4h: commodity avg `0.2682` n `13`; crypto_alt avg `1.181` n `239`; crypto_major avg `0.5653` n `8`; equity avg `0.5603` n `157`; fx avg `0.053` n `6`; index avg `0.0282` n `27`; metal avg `-0.0909` n `20`; unknown avg `1.8386` n `1212`
- 24h: commodity avg `-0.1442` n `13`; crypto_alt avg `-1.3118` n `238`; crypto_major avg `-0.935` n `8`; equity avg `-3.5096` n `157`; fx avg `0.0281` n `6`; index avg `-0.251` n `27`; metal avg `-0.4455` n `20`; unknown avg `3.9551` n `1020`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
