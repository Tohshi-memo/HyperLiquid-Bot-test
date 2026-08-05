# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T19:52:27.810326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0461` n `12`; crypto_alt avg `-0.0449` n `230`; crypto_major avg `-0.009` n `8`; equity avg `-0.1809` n `108`; fx avg `0.0105` n `6`; index avg `-0.0185` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.0369` n `782`
- 1h: commodity avg `-0.018` n `12`; crypto_alt avg `-0.0214` n `230`; crypto_major avg `0.1222` n `8`; equity avg `-0.1515` n `108`; fx avg `0.0025` n `6`; index avg `-0.0221` n `25`; metal avg `-0.0526` n `20`; unknown avg `-0.1483` n `782`
- 4h: commodity avg `-0.1233` n `12`; crypto_alt avg `0.2573` n `230`; crypto_major avg `0.659` n `8`; equity avg `-0.1587` n `108`; fx avg `0.0033` n `6`; index avg `-0.0135` n `25`; metal avg `0.0876` n `20`; unknown avg `-0.1131` n `782`
- 24h: commodity avg `-0.1555` n `12`; crypto_alt avg `0.5227` n `230`; crypto_major avg `0.9243` n `8`; equity avg `-0.438` n `108`; fx avg `-0.0453` n `6`; index avg `-0.1026` n `25`; metal avg `0.8066` n `20`; unknown avg `0.7916` n `749`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
