# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T01:22:27.990513+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `13`; crypto_alt avg `-0.1431` n `238`; crypto_major avg `-0.0771` n `8`; equity avg `-0.0412` n `156`; fx avg `0.0061` n `6`; index avg `-0.0042` n `27`; metal avg `-0.0056` n `20`; unknown avg `-0.0425` n `1262`
- 1h: commodity avg `-0.0426` n `13`; crypto_alt avg `-0.2373` n `238`; crypto_major avg `-0.0358` n `8`; equity avg `0.0288` n `156`; fx avg `0.0123` n `6`; index avg `-0.0061` n `27`; metal avg `-0.0068` n `20`; unknown avg `-0.2544` n `1254`
- 4h: commodity avg `-0.0739` n `13`; crypto_alt avg `0.9387` n `238`; crypto_major avg `0.5954` n `8`; equity avg `0.2945` n `156`; fx avg `-0.0032` n `6`; index avg `0.0468` n `27`; metal avg `0.0461` n `20`; unknown avg `4.1415` n `1249`
- 24h: commodity avg `-0.0095` n `13`; crypto_alt avg `4.4999` n `238`; crypto_major avg `1.6097` n `8`; equity avg `-1.5071` n `156`; fx avg `-0.1396` n `6`; index avg `-0.0609` n `27`; metal avg `-0.6909` n `20`; unknown avg `3.6626` n `1018`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
