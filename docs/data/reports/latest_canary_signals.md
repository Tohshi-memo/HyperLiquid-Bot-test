# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T10:52:34.775644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0324` n `13`; crypto_alt avg `-0.1452` n `235`; crypto_major avg `-0.1477` n `8`; equity avg `0.0514` n `150`; fx avg `0.0081` n `6`; index avg `0.0268` n `26`; metal avg `0.0935` n `20`; unknown avg `1.3343` n `1077`
- 1h: commodity avg `0.1718` n `13`; crypto_alt avg `-0.784` n `235`; crypto_major avg `-0.6287` n `8`; equity avg `-0.4192` n `150`; fx avg `0.0267` n `6`; index avg `-0.0602` n `26`; metal avg `-0.0277` n `20`; unknown avg `2.1834` n `1075`
- 4h: commodity avg `0.4347` n `13`; crypto_alt avg `0.0738` n `235`; crypto_major avg `-0.383` n `8`; equity avg `-0.5116` n `150`; fx avg `0.0597` n `6`; index avg `-0.0814` n `26`; metal avg `-0.1168` n `20`; unknown avg `1.5236` n `1059`
- 24h: commodity avg `0.8746` n `13`; crypto_alt avg `0.0707` n `235`; crypto_major avg `-1.8191` n `8`; equity avg `-1.6459` n `150`; fx avg `0.0351` n `6`; index avg `-0.2833` n `26`; metal avg `-0.1115` n `20`; unknown avg `416.6783` n `974`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
