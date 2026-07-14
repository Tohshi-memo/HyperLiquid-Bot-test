# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T11:07:25.807204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0496` n `12`; crypto_alt avg `-0.0646` n `230`; crypto_major avg `-0.0669` n `8`; equity avg `-0.3712` n `92`; fx avg `0.0022` n `6`; index avg `-0.0179` n `25`; metal avg `-0.0303` n `20`; unknown avg `0.0194` n `766`
- 1h: commodity avg `-0.0384` n `12`; crypto_alt avg `-0.0547` n `230`; crypto_major avg `0.1226` n `8`; equity avg `-0.4156` n `92`; fx avg `0.0032` n `6`; index avg `-0.0097` n `25`; metal avg `-0.094` n `20`; unknown avg `-0.0055` n `766`
- 4h: commodity avg `0.2035` n `12`; crypto_alt avg `-0.1749` n `230`; crypto_major avg `0.251` n `8`; equity avg `-0.1365` n `92`; fx avg `0.0431` n `6`; index avg `0.0249` n `25`; metal avg `-0.1631` n `20`; unknown avg `-0.0844` n `766`
- 24h: commodity avg `1.4714` n `12`; crypto_alt avg `-1.0519` n `230`; crypto_major avg `-0.5544` n `8`; equity avg `-1.0144` n `92`; fx avg `-0.0308` n `6`; index avg `-0.1442` n `25`; metal avg `-0.2294` n `20`; unknown avg `-0.3012` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
