# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T20:37:33.370871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `13`; crypto_alt avg `0.0666` n `235`; crypto_major avg `0.019` n `8`; equity avg `0.0165` n `150`; fx avg `-0.0021` n `6`; index avg `-0.0013` n `26`; metal avg `0.0018` n `20`; unknown avg `2.5536` n `1134`
- 1h: commodity avg `0.0336` n `13`; crypto_alt avg `0.134` n `235`; crypto_major avg `-0.0424` n `8`; equity avg `0.0173` n `150`; fx avg `0.0026` n `6`; index avg `-0.0056` n `26`; metal avg `0.0154` n `20`; unknown avg `0.1799` n `1118`
- 4h: commodity avg `0.0836` n `13`; crypto_alt avg `0.1028` n `235`; crypto_major avg `-0.372` n `8`; equity avg `0.0277` n `150`; fx avg `0.0089` n `6`; index avg `0.0085` n `26`; metal avg `0.0351` n `20`; unknown avg `0.3355` n `1100`
- 24h: commodity avg `0.3244` n `13`; crypto_alt avg `1.9228` n `235`; crypto_major avg `0.6845` n `8`; equity avg `0.3016` n `150`; fx avg `0.0232` n `6`; index avg `0.0294` n `26`; metal avg `0.0888` n `20`; unknown avg `0.9567` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
