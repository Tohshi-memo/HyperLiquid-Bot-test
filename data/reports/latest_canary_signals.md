# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T13:52:36.722295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0867` n `13`; crypto_alt avg `0.329` n `235`; crypto_major avg `0.3405` n `8`; equity avg `0.0726` n `150`; fx avg `-0.0077` n `6`; index avg `-0.0026` n `26`; metal avg `0.0937` n `20`; unknown avg `2.9443` n `1058`
- 1h: commodity avg `0.0791` n `13`; crypto_alt avg `0.047` n `235`; crypto_major avg `0.0325` n `8`; equity avg `-0.203` n `150`; fx avg `0.0335` n `6`; index avg `-0.0826` n `26`; metal avg `0.0727` n `20`; unknown avg `16.7805` n `1056`
- 4h: commodity avg `0.1474` n `13`; crypto_alt avg `-0.7314` n `235`; crypto_major avg `-0.628` n `8`; equity avg `-0.6773` n `150`; fx avg `-0.0387` n `6`; index avg `-0.1929` n `26`; metal avg `-0.2184` n `20`; unknown avg `6.6437` n `1050`
- 24h: commodity avg `1.2075` n `13`; crypto_alt avg `-5.5742` n `235`; crypto_major avg `-4.0044` n `8`; equity avg `-2.1384` n `150`; fx avg `-0.1522` n `6`; index avg `-0.459` n `26`; metal avg `-0.6027` n `20`; unknown avg `816.0725` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
