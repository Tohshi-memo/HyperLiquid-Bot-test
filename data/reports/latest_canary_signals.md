# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T20:37:27.222571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0082` n `13`; crypto_alt avg `-0.1339` n `237`; crypto_major avg `-0.002` n `8`; equity avg `-0.0031` n `151`; fx avg `0.0237` n `6`; index avg `-0.0053` n `26`; metal avg `-0.0028` n `20`; unknown avg `12.3711` n `1194`
- 1h: commodity avg `0.0433` n `13`; crypto_alt avg `-0.3117` n `237`; crypto_major avg `-0.0893` n `8`; equity avg `-0.0086` n `151`; fx avg `-0.0218` n `6`; index avg `-0.0164` n `26`; metal avg `-0.0355` n `20`; unknown avg `11.8281` n `1178`
- 4h: commodity avg `0.0425` n `13`; crypto_alt avg `-1.7722` n `237`; crypto_major avg `-0.7285` n `8`; equity avg `-0.2697` n `151`; fx avg `-0.0109` n `6`; index avg `-0.0515` n `26`; metal avg `-0.0505` n `20`; unknown avg `2.7166` n `1158`
- 24h: commodity avg `0.0826` n `13`; crypto_alt avg `-5.2315` n `236`; crypto_major avg `-2.4537` n `8`; equity avg `-1.2313` n `151`; fx avg `-0.022` n `6`; index avg `-0.1692` n `26`; metal avg `-0.1052` n `20`; unknown avg `2.0058` n `1007`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.21`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1431`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1395`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1193`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0791`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
