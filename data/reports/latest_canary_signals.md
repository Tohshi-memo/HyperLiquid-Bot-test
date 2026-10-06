# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T23:22:33.179952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `13`; crypto_alt avg `0.0962` n `235`; crypto_major avg `0.0176` n `8`; equity avg `0.0173` n `150`; fx avg `-0.0022` n `6`; index avg `0.0019` n `26`; metal avg `0.0119` n `20`; unknown avg `0.0968` n `1076`
- 1h: commodity avg `0.0232` n `13`; crypto_alt avg `0.1029` n `235`; crypto_major avg `-0.1147` n `8`; equity avg `-0.0053` n `150`; fx avg `0.0008` n `6`; index avg `-0.0024` n `26`; metal avg `0.003` n `20`; unknown avg `0.1122` n `1074`
- 4h: commodity avg `0.1053` n `13`; crypto_alt avg `0.1344` n `235`; crypto_major avg `0.1288` n `8`; equity avg `0.075` n `150`; fx avg `-0.0103` n `6`; index avg `0.0056` n `26`; metal avg `-0.0494` n `20`; unknown avg `0.2865` n `990`
- 24h: commodity avg `0.3627` n `13`; crypto_alt avg `-1.1885` n `235`; crypto_major avg `-0.9968` n `8`; equity avg `0.347` n `149`; fx avg `0.0908` n `6`; index avg `-0.0188` n `26`; metal avg `0.0545` n `20`; unknown avg `871.1186` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
