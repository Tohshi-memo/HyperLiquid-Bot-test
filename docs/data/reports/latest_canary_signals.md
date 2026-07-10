# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T19:52:24.597314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `12`; crypto_alt avg `-0.0617` n `229`; crypto_major avg `-0.0642` n `8`; equity avg `-0.0814` n `92`; fx avg `0.0032` n `6`; index avg `-0.0016` n `25`; metal avg `0.0254` n `20`; unknown avg `0.1541` n `765`
- 1h: commodity avg `0.0047` n `12`; crypto_alt avg `0.3075` n `229`; crypto_major avg `0.3738` n `8`; equity avg `-0.0381` n `92`; fx avg `0.0041` n `6`; index avg `-0.005` n `25`; metal avg `0.0463` n `20`; unknown avg `0.1073` n `765`
- 4h: commodity avg `0.341` n `12`; crypto_alt avg `0.2457` n `229`; crypto_major avg `0.2109` n `8`; equity avg `0.29` n `92`; fx avg `-0.0297` n `6`; index avg `0.0939` n `25`; metal avg `-0.0208` n `20`; unknown avg `-0.1061` n `765`
- 24h: commodity avg `-0.2246` n `12`; crypto_alt avg `0.6736` n `229`; crypto_major avg `0.9311` n `8`; equity avg `-0.5301` n `92`; fx avg `-0.1545` n `6`; index avg `0.0358` n `25`; metal avg `0.105` n `20`; unknown avg `-0.1913` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
