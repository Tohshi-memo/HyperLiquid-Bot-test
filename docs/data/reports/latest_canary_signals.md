# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T22:37:29.642948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1566` n `12`; crypto_alt avg `-0.1383` n `234`; crypto_major avg `-0.0613` n `8`; equity avg `-0.0388` n `142`; fx avg `0.0143` n `6`; index avg `-0.0178` n `26`; metal avg `-0.0328` n `20`; unknown avg `0.2296` n `962`
- 1h: commodity avg `0.0585` n `12`; crypto_alt avg `-0.1558` n `234`; crypto_major avg `0.1874` n `8`; equity avg `0.0556` n `142`; fx avg `0.0151` n `6`; index avg `0.0351` n `26`; metal avg `0.0023` n `20`; unknown avg `0.4308` n `934`
- 4h: commodity avg `0.0438` n `12`; crypto_alt avg `-0.1543` n `234`; crypto_major avg `0.0068` n `8`; equity avg `0.2285` n `142`; fx avg `0.0081` n `6`; index avg `0.0832` n `26`; metal avg `0.0887` n `20`; unknown avg `1.5404` n `872`
- 24h: commodity avg `-0.8707` n `12`; crypto_alt avg `1.0181` n `234`; crypto_major avg `0.0461` n `8`; equity avg `0.7628` n `142`; fx avg `-0.1568` n `6`; index avg `0.0981` n `26`; metal avg `0.2507` n `20`; unknown avg `3099.5013` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1766`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
