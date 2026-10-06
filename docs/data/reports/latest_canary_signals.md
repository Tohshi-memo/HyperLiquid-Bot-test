# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T07:52:29.122755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0226` n `13`; crypto_alt avg `0.1158` n `235`; crypto_major avg `0.1149` n `8`; equity avg `0.006` n `149`; fx avg `-0.024` n `6`; index avg `0.0033` n `26`; metal avg `0.0172` n `20`; unknown avg `4.8878` n `1074`
- 1h: commodity avg `0.0532` n `13`; crypto_alt avg `0.2557` n `235`; crypto_major avg `0.1433` n `8`; equity avg `-0.0183` n `149`; fx avg `0.0154` n `6`; index avg `0.0036` n `26`; metal avg `0.0279` n `20`; unknown avg `5.4812` n `1008`
- 4h: commodity avg `-0.2467` n `13`; crypto_alt avg `0.5726` n `235`; crypto_major avg `-0.0142` n `8`; equity avg `0.1315` n `149`; fx avg `0.0066` n `6`; index avg `0.0461` n `26`; metal avg `-0.0139` n `20`; unknown avg `1.9889` n `986`
- 24h: commodity avg `-0.253` n `13`; crypto_alt avg `-1.3871` n `235`; crypto_major avg `-0.969` n `8`; equity avg `0.185` n `149`; fx avg `0.0328` n `6`; index avg `0.1431` n `26`; metal avg `-0.2024` n `20`; unknown avg `-0.3052` n `830`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.188`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
