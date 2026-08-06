# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T07:52:29.888920+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `-0.0884` n `230`; crypto_major avg `-0.139` n `8`; equity avg `-0.0584` n `108`; fx avg `0.0025` n `6`; index avg `-0.0288` n `25`; metal avg `-0.0816` n `20`; unknown avg `-0.0296` n `782`
- 1h: commodity avg `0.0013` n `12`; crypto_alt avg `-0.0176` n `230`; crypto_major avg `-0.1468` n `8`; equity avg `-0.0063` n `108`; fx avg `0.0232` n `6`; index avg `-0.0041` n `25`; metal avg `-0.026` n `20`; unknown avg `0.0435` n `782`
- 4h: commodity avg `0.1285` n `12`; crypto_alt avg `0.4362` n `230`; crypto_major avg `0.238` n `8`; equity avg `-0.1126` n `108`; fx avg `0.1148` n `6`; index avg `-0.0396` n `25`; metal avg `-0.1107` n `20`; unknown avg `0.091` n `750`
- 24h: commodity avg `-0.1204` n `12`; crypto_alt avg `0.2179` n `230`; crypto_major avg `-0.0628` n `8`; equity avg `-1.8809` n `108`; fx avg `0.0542` n `6`; index avg `-0.3757` n `25`; metal avg `0.076` n `20`; unknown avg `0.8679` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1909`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
