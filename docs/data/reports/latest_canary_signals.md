# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T07:07:16.942837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1408` n `12`; crypto_alt avg `-0.079` n `228`; crypto_major avg `0.0041` n `8`; equity avg `0.1504` n `66`; fx avg `-0.0003` n `5`; index avg `0.0576` n `23`; metal avg `0.1503` n `18`; unknown avg `-0.1875` n `383`
- 1h: commodity avg `-0.1173` n `12`; crypto_alt avg `-0.1999` n `228`; crypto_major avg `-0.0892` n `8`; equity avg `0.1904` n `66`; fx avg `-0.0175` n `5`; index avg `0.1063` n `23`; metal avg `0.5275` n `18`; unknown avg `0.7365` n `383`
- 4h: commodity avg `-0.088` n `12`; crypto_alt avg `-0.9461` n `228`; crypto_major avg `-0.6256` n `8`; equity avg `0.122` n `66`; fx avg `-0.0338` n `5`; index avg `0.168` n `23`; metal avg `0.6372` n `18`; unknown avg `0.4368` n `363`
- 24h: commodity avg `2.583` n `12`; crypto_alt avg `-11.3689` n `228`; crypto_major avg `-3.7408` n `8`; equity avg `-2.9358` n `65`; fx avg `-0.1118` n `5`; index avg `-1.6664` n `23`; metal avg `-5.8148` n `18`; unknown avg `-0.5886` n `357`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
