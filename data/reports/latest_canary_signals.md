# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T11:07:26.891358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1468` n `13`; crypto_alt avg `-0.3828` n `239`; crypto_major avg `-0.3902` n `8`; equity avg `-0.2585` n `163`; fx avg `-0.0066` n `6`; index avg `-0.038` n `27`; metal avg `-0.0511` n `20`; unknown avg `0.3336` n `1260`
- 1h: commodity avg `0.1321` n `13`; crypto_alt avg `-0.3451` n `239`; crypto_major avg `-0.617` n `8`; equity avg `-0.3938` n `163`; fx avg `-0.0087` n `6`; index avg `-0.0424` n `27`; metal avg `-0.072` n `20`; unknown avg `0.7344` n `1262`
- 4h: commodity avg `0.2937` n `13`; crypto_alt avg `-0.2793` n `239`; crypto_major avg `-0.5368` n `8`; equity avg `0.1903` n `163`; fx avg `-0.0292` n `6`; index avg `0.0536` n `27`; metal avg `-0.2255` n `20`; unknown avg `150.0715` n `1188`
- 24h: commodity avg `-0.0903` n `13`; crypto_alt avg `0.5078` n `239`; crypto_major avg `0.6171` n `8`; equity avg `1.159` n `163`; fx avg `-0.0846` n `6`; index avg `0.1005` n `27`; metal avg `-1.0476` n `20`; unknown avg `6.4203` n `1097`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
