# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T13:07:31.410828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0417` n `12`; crypto_alt avg `0.5287` n `234`; crypto_major avg `0.3566` n `8`; equity avg `0.1317` n `141`; fx avg `-0.031` n `6`; index avg `0.02` n `26`; metal avg `-0.0063` n `20`; unknown avg `0.6105` n `943`
- 1h: commodity avg `-0.0547` n `12`; crypto_alt avg `0.7765` n `234`; crypto_major avg `0.499` n `8`; equity avg `0.0411` n `141`; fx avg `-0.0347` n `6`; index avg `0.0253` n `26`; metal avg `0.0285` n `20`; unknown avg `1.6962` n `943`
- 4h: commodity avg `-0.1355` n `12`; crypto_alt avg `0.3889` n `234`; crypto_major avg `0.0907` n `8`; equity avg `0.2345` n `141`; fx avg `-0.0804` n `6`; index avg `0.0475` n `26`; metal avg `0.0141` n `20`; unknown avg `3.1629` n `937`
- 24h: commodity avg `0.4541` n `12`; crypto_alt avg `-3.1681` n `234`; crypto_major avg `-2.6048` n `8`; equity avg `-2.0133` n `141`; fx avg `-0.0379` n `6`; index avg `-0.3724` n `26`; metal avg `-0.2978` n `20`; unknown avg `585.2201` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
