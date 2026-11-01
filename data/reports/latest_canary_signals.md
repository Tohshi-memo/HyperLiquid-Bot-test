# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T15:04:55.331101+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `13`; crypto_alt avg `-0.0941` n `238`; crypto_major avg `-0.0442` n `8`; equity avg `0.006` n `156`; fx avg `-0.0013` n `6`; index avg `0.0045` n `27`; metal avg `0.0` n `20`; unknown avg `-0.1939` n `1257`
- 1h: commodity avg `0.0171` n `13`; crypto_alt avg `-0.1741` n `238`; crypto_major avg `-0.0565` n `8`; equity avg `-0.0081` n `156`; fx avg `0.002` n `6`; index avg `0.025` n `27`; metal avg `-0.0067` n `20`; unknown avg `3.1769` n `1257`
- 4h: commodity avg `0.0479` n `13`; crypto_alt avg `0.0842` n `238`; crypto_major avg `0.016` n `8`; equity avg `-0.0038` n `156`; fx avg `0.0166` n `6`; index avg `0.0396` n `27`; metal avg `-0.0022` n `20`; unknown avg `-0.0803` n `1251`
- 24h: commodity avg `0.0823` n `13`; crypto_alt avg `0.3045` n `238`; crypto_major avg `0.6162` n `8`; equity avg `0.4605` n `156`; fx avg `-0.0081` n `6`; index avg `0.0745` n `27`; metal avg `0.0547` n `20`; unknown avg `3.4221` n `1018`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
