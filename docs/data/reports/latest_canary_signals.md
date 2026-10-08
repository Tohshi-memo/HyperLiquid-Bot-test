# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T06:52:29.506952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0778` n `13`; crypto_alt avg `0.3052` n `235`; crypto_major avg `0.2159` n `8`; equity avg `-0.0252` n `150`; fx avg `0.0168` n `6`; index avg `-0.0157` n `26`; metal avg `0.0557` n `20`; unknown avg `0.3226` n `1077`
- 1h: commodity avg `0.1779` n `13`; crypto_alt avg `0.2595` n `235`; crypto_major avg `0.1091` n `8`; equity avg `-0.404` n `150`; fx avg `0.0027` n `6`; index avg `-0.11` n `26`; metal avg `-0.0149` n `20`; unknown avg `0.3127` n `1047`
- 4h: commodity avg `0.2852` n `13`; crypto_alt avg `-0.8401` n `235`; crypto_major avg `-0.8926` n `8`; equity avg `-1.0815` n `150`; fx avg `-0.0034` n `6`; index avg `-0.2059` n `26`; metal avg `-0.2369` n `20`; unknown avg `1.6528` n `1041`
- 24h: commodity avg `0.5676` n `13`; crypto_alt avg `-1.2061` n `235`; crypto_major avg `-2.4561` n `8`; equity avg `-1.8833` n `150`; fx avg `-0.119` n `6`; index avg `-0.3204` n `26`; metal avg `-0.194` n `20`; unknown avg `417.2374` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
