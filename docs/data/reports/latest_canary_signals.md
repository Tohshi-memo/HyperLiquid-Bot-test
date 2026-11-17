# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T12:37:32.371376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0242` n `13`; crypto_alt avg `0.1321` n `239`; crypto_major avg `0.1622` n `8`; equity avg `0.1588` n `162`; fx avg `-0.0001` n `6`; index avg `0.0042` n `27`; metal avg `-0.0636` n `20`; unknown avg `0.1173` n `1266`
- 1h: commodity avg `0.0651` n `13`; crypto_alt avg `0.2667` n `239`; crypto_major avg `0.205` n `8`; equity avg `0.6097` n `162`; fx avg `0.0178` n `6`; index avg `0.0118` n `27`; metal avg `-0.0428` n `20`; unknown avg `0.2288` n `1254`
- 4h: commodity avg `0.2399` n `13`; crypto_alt avg `0.8351` n `239`; crypto_major avg `0.7409` n `8`; equity avg `1.1908` n `162`; fx avg `-0.0131` n `6`; index avg `0.0942` n `27`; metal avg `0.0176` n `20`; unknown avg `19.7016` n `1256`
- 24h: commodity avg `-0.5393` n `13`; crypto_alt avg `2.3487` n `239`; crypto_major avg `2.3394` n `8`; equity avg `-0.378` n `162`; fx avg `-0.0323` n `6`; index avg `-0.0813` n `27`; metal avg `-0.1516` n `20`; unknown avg `5.8691` n `1115`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
