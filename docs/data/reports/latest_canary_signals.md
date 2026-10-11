# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T18:07:28.776655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `13`; crypto_alt avg `-0.1917` n `235`; crypto_major avg `-0.1429` n `8`; equity avg `-0.0189` n `150`; fx avg `-0.0027` n `6`; index avg `-0.0048` n `26`; metal avg `-0.0129` n `20`; unknown avg `0.1872` n `1130`
- 1h: commodity avg `0.0013` n `13`; crypto_alt avg `-0.0391` n `235`; crypto_major avg `0.0749` n `8`; equity avg `0.0047` n `150`; fx avg `-0.0075` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0135` n `20`; unknown avg `2.1251` n `1124`
- 4h: commodity avg `-0.0277` n `13`; crypto_alt avg `1.9256` n `235`; crypto_major avg `1.4166` n `8`; equity avg `0.2704` n `150`; fx avg `0.0117` n `6`; index avg `0.0345` n `26`; metal avg `0.0494` n `20`; unknown avg `23.291` n `1102`
- 24h: commodity avg `0.2659` n `13`; crypto_alt avg `2.2561` n `235`; crypto_major avg `1.0692` n `8`; equity avg `0.3337` n `150`; fx avg `0.0179` n `6`; index avg `0.0369` n `26`; metal avg `0.0809` n `20`; unknown avg `0.7437` n `917`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
