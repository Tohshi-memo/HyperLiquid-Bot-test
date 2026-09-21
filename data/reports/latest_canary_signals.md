# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T20:52:36.522201+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0059` n `12`; crypto_alt avg `-0.0353` n `234`; crypto_major avg `0.1627` n `8`; equity avg `0.0002` n `140`; fx avg `0.0042` n `6`; index avg `0.0015` n `26`; metal avg `0.0077` n `20`; unknown avg `17.3476` n `944`
- 1h: commodity avg `0.0027` n `12`; crypto_alt avg `0.3917` n `234`; crypto_major avg `0.9847` n `8`; equity avg `-0.0211` n `140`; fx avg `-0.0155` n `6`; index avg `-0.0325` n `26`; metal avg `-0.0204` n `20`; unknown avg `54.143` n `852`
- 4h: commodity avg `0.1507` n `12`; crypto_alt avg `0.1707` n `234`; crypto_major avg `1.3105` n `8`; equity avg `0.1968` n `140`; fx avg `0.0027` n `6`; index avg `0.038` n `26`; metal avg `0.0382` n `20`; unknown avg `14.9943` n `852`
- 24h: commodity avg `-1.0417` n `12`; crypto_alt avg `4.021` n `234`; crypto_major avg `6.301` n `8`; equity avg `2.7743` n `140`; fx avg `-0.0922` n `6`; index avg `0.6016` n `26`; metal avg `0.0401` n `20`; unknown avg `15.4576` n `731`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
