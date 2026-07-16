# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T09:37:28.533119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1774` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0456` n `12`; crypto_alt avg `-0.0204` n `230`; crypto_major avg `-0.0017` n `8`; equity avg `-0.095` n `94`; fx avg `-0.0145` n `6`; index avg `-0.0153` n `25`; metal avg `-0.0038` n `20`; unknown avg `-0.0332` n `768`
- 1h: commodity avg `-0.0289` n `12`; crypto_alt avg `-0.1473` n `230`; crypto_major avg `-0.2643` n `8`; equity avg `0.1179` n `94`; fx avg `-0.0117` n `6`; index avg `0.0197` n `25`; metal avg `0.044` n `20`; unknown avg `-0.1052` n `762`
- 4h: commodity avg `-0.0159` n `12`; crypto_alt avg `-1.047` n `230`; crypto_major avg `-1.2309` n `8`; equity avg `-0.7116` n `94`; fx avg `-0.064` n `6`; index avg `-0.0535` n `25`; metal avg `-0.0351` n `20`; unknown avg `-0.1054` n `746`
- 24h: commodity avg `-0.157` n `12`; crypto_alt avg `-0.8337` n `230`; crypto_major avg `-0.9999` n `8`; equity avg `-2.7137` n `93`; fx avg `0.0425` n `6`; index avg `-0.4429` n `25`; metal avg `-0.0043` n `20`; unknown avg `-0.1383` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
