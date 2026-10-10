# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T04:52:25.986967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `13`; crypto_alt avg `0.054` n `235`; crypto_major avg `0.0538` n `8`; equity avg `0.0096` n `150`; fx avg `0.0` n `6`; index avg `0.0014` n `26`; metal avg `-0.0013` n `20`; unknown avg `-0.0981` n `1116`
- 1h: commodity avg `0.0233` n `13`; crypto_alt avg `0.2578` n `235`; crypto_major avg `0.1464` n `8`; equity avg `0.0281` n `150`; fx avg `0.0068` n `6`; index avg `0.0098` n `26`; metal avg `-0.0035` n `20`; unknown avg `-0.2753` n `1108`
- 4h: commodity avg `0.0127` n `13`; crypto_alt avg `0.4076` n `235`; crypto_major avg `0.2003` n `8`; equity avg `0.0452` n `150`; fx avg `0.0032` n `6`; index avg `0.0134` n `26`; metal avg `-0.0132` n `20`; unknown avg `-0.1773` n `1108`
- 24h: commodity avg `0.0504` n `13`; crypto_alt avg `2.1378` n `235`; crypto_major avg `0.3635` n `8`; equity avg `0.4582` n `150`; fx avg `-0.0198` n `6`; index avg `0.0651` n `26`; metal avg `0.1688` n `20`; unknown avg `12.7106` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
