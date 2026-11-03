# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T02:52:32.588071+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0346` n `13`; crypto_alt avg `-0.3828` n `239`; crypto_major avg `-0.2994` n `8`; equity avg `-0.1539` n `157`; fx avg `-0.0018` n `6`; index avg `-0.0275` n `27`; metal avg `0.0184` n `20`; unknown avg `3.7286` n `1264`
- 1h: commodity avg `0.0237` n `13`; crypto_alt avg `-0.5335` n `239`; crypto_major avg `-0.4064` n `8`; equity avg `-0.2281` n `157`; fx avg `-0.0494` n `6`; index avg `-0.0489` n `27`; metal avg `-0.072` n `20`; unknown avg `-0.1975` n `1258`
- 4h: commodity avg `0.0701` n `13`; crypto_alt avg `-0.7021` n `239`; crypto_major avg `-0.2082` n `8`; equity avg `0.3224` n `157`; fx avg `-0.0804` n `6`; index avg `0.0603` n `27`; metal avg `-0.1044` n `20`; unknown avg `-0.7475` n `1246`
- 24h: commodity avg `-1.0059` n `13`; crypto_alt avg `-3.3045` n `238`; crypto_major avg `-2.037` n `8`; equity avg `-3.1907` n `157`; fx avg `0.0085` n `6`; index avg `-0.168` n `27`; metal avg `0.1866` n `20`; unknown avg `12.2931` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
