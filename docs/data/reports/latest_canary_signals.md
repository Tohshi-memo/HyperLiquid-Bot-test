# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T00:52:29.081784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0489` n `12`; crypto_alt avg `-0.1286` n `230`; crypto_major avg `-0.0918` n `8`; equity avg `0.132` n `102`; fx avg `-0.0886` n `6`; index avg `0.0208` n `25`; metal avg `-0.0041` n `20`; unknown avg `-0.0265` n `784`
- 1h: commodity avg `0.0541` n `12`; crypto_alt avg `-0.3218` n `230`; crypto_major avg `-0.341` n `8`; equity avg `0.0334` n `102`; fx avg `-0.2732` n `6`; index avg `-0.143` n `25`; metal avg `-0.0944` n `20`; unknown avg `0.0039` n `784`
- 4h: commodity avg `-0.0555` n `12`; crypto_alt avg `-0.4173` n `230`; crypto_major avg `-0.307` n `8`; equity avg `0.2846` n `102`; fx avg `-0.2511` n `6`; index avg `-0.0862` n `25`; metal avg `-0.2432` n `20`; unknown avg `1.614` n `783`
- 24h: commodity avg `-1.108` n `12`; crypto_alt avg `0.6237` n `230`; crypto_major avg `1.2254` n `8`; equity avg `1.462` n `102`; fx avg `-0.2873` n `6`; index avg `0.1635` n `25`; metal avg `0.0996` n `20`; unknown avg `1.5397` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
