# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T02:52:31.931341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `13`; crypto_alt avg `0.1075` n `238`; crypto_major avg `0.0903` n `8`; equity avg `0.0205` n `156`; fx avg `-0.0157` n `6`; index avg `0.0004` n `27`; metal avg `0.0209` n `20`; unknown avg `-0.0536` n `1260`
- 1h: commodity avg `0.0987` n `13`; crypto_alt avg `-0.1082` n `238`; crypto_major avg `0.0938` n `8`; equity avg `-0.0208` n `156`; fx avg `-0.0124` n `6`; index avg `-0.007` n `27`; metal avg `-0.0096` n `20`; unknown avg `0.026` n `1252`
- 4h: commodity avg `-0.0236` n `13`; crypto_alt avg `0.1186` n `238`; crypto_major avg `0.4856` n `8`; equity avg `0.1813` n `156`; fx avg `0.0054` n `6`; index avg `0.0074` n `27`; metal avg `-0.0048` n `20`; unknown avg `-0.0296` n `1245`
- 24h: commodity avg `-0.0795` n `13`; crypto_alt avg `3.936` n `238`; crypto_major avg `0.7991` n `8`; equity avg `-2.0648` n `156`; fx avg `-0.1476` n `6`; index avg `-0.0717` n `27`; metal avg `-0.6194` n `20`; unknown avg `-0.8328` n `1014`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
