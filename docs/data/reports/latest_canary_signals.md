# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T05:22:17.690255+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0466` n `12`; crypto_alt avg `-0.1702` n `228`; crypto_major avg `-0.1562` n `8`; equity avg `-0.1485` n `66`; fx avg `-0.0141` n `5`; index avg `-0.1208` n `23`; metal avg `0.1464` n `18`; unknown avg `0.5408` n `383`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `0.1488` n `228`; crypto_major avg `0.1493` n `8`; equity avg `-0.1549` n `66`; fx avg `-0.0161` n `5`; index avg `-0.1637` n `23`; metal avg `-0.0322` n `18`; unknown avg `-0.7523` n `383`
- 4h: commodity avg `-0.2354` n `12`; crypto_alt avg `0.4108` n `228`; crypto_major avg `-0.0341` n `8`; equity avg `0.5564` n `66`; fx avg `0.0438` n `5`; index avg `0.1609` n `23`; metal avg `0.7919` n `18`; unknown avg `-1.0302` n `383`
- 24h: commodity avg `2.7346` n `12`; crypto_alt avg `-10.8056` n `228`; crypto_major avg `-3.3335` n `8`; equity avg `-3.1154` n `65`; fx avg `-0.0765` n `5`; index avg `-1.8319` n `23`; metal avg `-6.0589` n `18`; unknown avg `550.0814` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
