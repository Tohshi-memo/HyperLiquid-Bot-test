# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T07:52:29.720277+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `13`; crypto_alt avg `-0.2022` n `237`; crypto_major avg `-0.2624` n `8`; equity avg `-0.1916` n `151`; fx avg `-0.0029` n `6`; index avg `-0.0312` n `26`; metal avg `-0.0976` n `20`; unknown avg `0.7387` n `1195`
- 1h: commodity avg `-0.0291` n `13`; crypto_alt avg `0.2099` n `237`; crypto_major avg `-0.0741` n `8`; equity avg `-0.139` n `151`; fx avg `-0.0128` n `6`; index avg `-0.0338` n `26`; metal avg `-0.0726` n `20`; unknown avg `0.1337` n `1190`
- 4h: commodity avg `-0.0372` n `13`; crypto_alt avg `0.3828` n `237`; crypto_major avg `0.2314` n `8`; equity avg `-0.0481` n `151`; fx avg `-0.0615` n `6`; index avg `-0.0168` n `26`; metal avg `-0.1128` n `20`; unknown avg `2.9668` n `1162`
- 24h: commodity avg `-0.5002` n `13`; crypto_alt avg `0.6763` n `237`; crypto_major avg `1.2693` n `8`; equity avg `2.6517` n `151`; fx avg `-0.0599` n `6`; index avg `0.4692` n `26`; metal avg `0.2158` n `20`; unknown avg `2.4341` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1937`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1188`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0641`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0628`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
