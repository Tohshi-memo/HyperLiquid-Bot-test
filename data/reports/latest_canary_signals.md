# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T00:37:30.764646+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0494` n `12`; crypto_alt avg `-0.0124` n `228`; crypto_major avg `-0.0361` n `8`; equity avg `0.0111` n `74`; fx avg `-0.0048` n `6`; index avg `-0.0356` n `23`; metal avg `-0.0174` n `18`; unknown avg `0.1224` n `643`
- 1h: commodity avg `0.0537` n `12`; crypto_alt avg `0.5374` n `228`; crypto_major avg `0.143` n `8`; equity avg `0.1289` n `74`; fx avg `0.0205` n `6`; index avg `0.072` n `23`; metal avg `0.0321` n `18`; unknown avg `-0.1319` n `643`
- 4h: commodity avg `-0.2223` n `12`; crypto_alt avg `-0.1087` n `228`; crypto_major avg `-0.6468` n `8`; equity avg `0.247` n `74`; fx avg `0.0552` n `6`; index avg `0.1749` n `23`; metal avg `-0.003` n `18`; unknown avg `0.888` n `643`
- 24h: commodity avg `-0.8076` n `12`; crypto_alt avg `-0.5155` n `228`; crypto_major avg `-0.3556` n `8`; equity avg `-0.9616` n `74`; fx avg `0.047` n `6`; index avg `0.4432` n `23`; metal avg `0.1964` n `18`; unknown avg `40.9731` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
