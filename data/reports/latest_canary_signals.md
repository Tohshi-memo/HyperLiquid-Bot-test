# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T10:07:29.131052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0397` n `12`; crypto_alt avg `0.0664` n `228`; crypto_major avg `-0.1253` n `8`; equity avg `0.0283` n `88`; fx avg `0.0106` n `6`; index avg `0.0018` n `23`; metal avg `0.0398` n `20`; unknown avg `-0.0113` n `765`
- 1h: commodity avg `0.1593` n `12`; crypto_alt avg `-0.0289` n `228`; crypto_major avg `-0.2605` n `8`; equity avg `0.0568` n `88`; fx avg `0.0366` n `6`; index avg `0.0062` n `23`; metal avg `0.1821` n `20`; unknown avg `0.0194` n `765`
- 4h: commodity avg `-0.1353` n `12`; crypto_alt avg `-0.1476` n `228`; crypto_major avg `-0.5912` n `8`; equity avg `-0.0503` n `88`; fx avg `0.0495` n `6`; index avg `-0.0099` n `23`; metal avg `0.2295` n `20`; unknown avg `0.1733` n `763`
- 24h: commodity avg `-0.4118` n `12`; crypto_alt avg `-0.0918` n `228`; crypto_major avg `-0.5383` n `8`; equity avg `0.6047` n `88`; fx avg `0.1289` n `6`; index avg `0.0097` n `23`; metal avg `-0.6442` n `20`; unknown avg `0.1956` n `743`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
