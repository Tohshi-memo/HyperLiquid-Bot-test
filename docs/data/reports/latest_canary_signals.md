# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T03:37:27.814347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0188` n `13`; crypto_alt avg `0.3497` n `238`; crypto_major avg `0.4698` n `8`; equity avg `0.2343` n `156`; fx avg `0.018` n `6`; index avg `0.0327` n `27`; metal avg `0.0379` n `20`; unknown avg `1.6281` n `1233`
- 1h: commodity avg `-0.0756` n `13`; crypto_alt avg `0.4818` n `238`; crypto_major avg `0.622` n `8`; equity avg `0.693` n `156`; fx avg `0.0523` n `6`; index avg `0.0832` n `27`; metal avg `0.0217` n `20`; unknown avg `1.206` n `1229`
- 4h: commodity avg `-0.3033` n `13`; crypto_alt avg `0.3576` n `238`; crypto_major avg `0.905` n `8`; equity avg `1.246` n `156`; fx avg `0.2103` n `6`; index avg `0.2912` n `27`; metal avg `-0.0377` n `20`; unknown avg `3.0735` n `1213`
- 24h: commodity avg `-0.4001` n `13`; crypto_alt avg `-0.1295` n `238`; crypto_major avg `0.919` n `8`; equity avg `1.5261` n `156`; fx avg `0.2249` n `6`; index avg `0.3378` n `27`; metal avg `0.0828` n `20`; unknown avg `3.8606` n `1096`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1861`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
