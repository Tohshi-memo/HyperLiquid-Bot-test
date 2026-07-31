# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T17:37:34.358869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0119` n `12`; crypto_alt avg `0.2609` n `230`; crypto_major avg `0.2927` n `8`; equity avg `0.4952` n `102`; fx avg `-0.0627` n `6`; index avg `0.0463` n `25`; metal avg `0.0587` n `20`; unknown avg `0.2585` n `780`
- 1h: commodity avg `0.0716` n `12`; crypto_alt avg `0.529` n `230`; crypto_major avg `0.3289` n `8`; equity avg `0.656` n `102`; fx avg `-0.0205` n `6`; index avg `0.0803` n `25`; metal avg `0.0762` n `20`; unknown avg `0.1414` n `780`
- 4h: commodity avg `-0.1737` n `12`; crypto_alt avg `0.3007` n `230`; crypto_major avg `-0.5633` n `8`; equity avg `-1.3921` n `102`; fx avg `0.0959` n `6`; index avg `-0.1774` n `25`; metal avg `0.2325` n `20`; unknown avg `-0.1654` n `780`
- 24h: commodity avg `0.0767` n `12`; crypto_alt avg `-0.0418` n `230`; crypto_major avg `-1.5661` n `8`; equity avg `0.9512` n `102`; fx avg `0.1475` n `6`; index avg `0.374` n `25`; metal avg `-0.2794` n `20`; unknown avg `0.4665` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
