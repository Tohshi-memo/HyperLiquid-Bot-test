# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T09:07:29.208330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `13`; crypto_alt avg `0.3677` n `235`; crypto_major avg `0.1706` n `8`; equity avg `0.0607` n `150`; fx avg `0.0081` n `6`; index avg `-0.0038` n `26`; metal avg `0.0035` n `20`; unknown avg `0.0734` n `1075`
- 1h: commodity avg `0.1163` n `13`; crypto_alt avg `0.2556` n `235`; crypto_major avg `-0.0128` n `8`; equity avg `0.0483` n `150`; fx avg `0.0043` n `6`; index avg `-0.0083` n `26`; metal avg `0.0189` n `20`; unknown avg `2.0737` n `1075`
- 4h: commodity avg `0.4529` n `13`; crypto_alt avg `0.6564` n `235`; crypto_major avg `0.2578` n `8`; equity avg `-0.7692` n `150`; fx avg `0.0263` n `6`; index avg `-0.1672` n `26`; metal avg `-0.1535` n `20`; unknown avg `0.8862` n `1031`
- 24h: commodity avg `0.792` n `13`; crypto_alt avg `-0.1` n `235`; crypto_major avg `-1.919` n `8`; equity avg `-1.4912` n `150`; fx avg `-0.009` n `6`; index avg `-0.2854` n `26`; metal avg `-0.0299` n `20`; unknown avg `416.7369` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
