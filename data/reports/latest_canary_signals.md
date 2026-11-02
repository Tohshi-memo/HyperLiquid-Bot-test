# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T04:37:28.542390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0604` n `13`; crypto_alt avg `-0.2212` n `238`; crypto_major avg `-0.2264` n `8`; equity avg `-0.0465` n `156`; fx avg `0.0005` n `6`; index avg `-0.0079` n `27`; metal avg `-0.0382` n `20`; unknown avg `0.0393` n `1263`
- 1h: commodity avg `-0.0242` n `13`; crypto_alt avg `-0.4156` n `238`; crypto_major avg `-0.2999` n `8`; equity avg `0.0413` n `156`; fx avg `-0.0081` n `6`; index avg `0.0378` n `27`; metal avg `-0.0294` n `20`; unknown avg `0.3416` n `1225`
- 4h: commodity avg `-0.3982` n `13`; crypto_alt avg `0.4382` n `238`; crypto_major avg `0.7614` n `8`; equity avg `1.011` n `156`; fx avg `0.1289` n `6`; index avg `0.1779` n `27`; metal avg `-0.0538` n `20`; unknown avg `1.7993` n `1195`
- 24h: commodity avg `-0.4259` n `13`; crypto_alt avg `-0.5416` n `238`; crypto_major avg `0.6281` n `8`; equity avg `1.5086` n `156`; fx avg `0.2263` n `6`; index avg `0.3697` n `27`; metal avg `0.0535` n `20`; unknown avg `3.5349` n `1074`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1722`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
