# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T19:08:45.199257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0084` n `13`; crypto_alt avg `0.1006` n `235`; crypto_major avg `-0.0127` n `8`; equity avg `0.0542` n `144`; fx avg `0.0083` n `6`; index avg `0.0151` n `26`; metal avg `0.0001` n `20`; unknown avg `-0.0949` n `1077`
- 1h: commodity avg `-0.1167` n `13`; crypto_alt avg `0.1965` n `235`; crypto_major avg `-0.0396` n `8`; equity avg `-0.0804` n `144`; fx avg `-0.0009` n `6`; index avg `0.0213` n `26`; metal avg `0.0187` n `20`; unknown avg `3.6313` n `1077`
- 4h: commodity avg `-0.37` n `13`; crypto_alt avg `0.2083` n `235`; crypto_major avg `-0.0405` n `8`; equity avg `0.08` n `144`; fx avg `-0.0134` n `6`; index avg `0.0764` n `26`; metal avg `0.0246` n `20`; unknown avg `2.7625` n `1071`
- 24h: commodity avg `-0.4524` n `13`; crypto_alt avg `0.0811` n `235`; crypto_major avg `0.1186` n `8`; equity avg `0.3068` n `144`; fx avg `-0.0854` n `6`; index avg `0.1431` n `26`; metal avg `0.2059` n `20`; unknown avg `4.1758` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2009`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
