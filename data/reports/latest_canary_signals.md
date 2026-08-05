# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T00:22:25.984266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0982` n `12`; crypto_alt avg `0.0829` n `230`; crypto_major avg `-0.0906` n `8`; equity avg `0.0732` n `108`; fx avg `0.001` n `6`; index avg `0.0323` n `25`; metal avg `-0.014` n `20`; unknown avg `-0.0065` n `781`
- 1h: commodity avg `0.075` n `12`; crypto_alt avg `-0.3835` n `230`; crypto_major avg `-0.5119` n `8`; equity avg `0.2559` n `108`; fx avg `-0.0341` n `6`; index avg `0.0588` n `25`; metal avg `0.0254` n `20`; unknown avg `0.3008` n `781`
- 4h: commodity avg `0.0726` n `12`; crypto_alt avg `-0.1144` n `230`; crypto_major avg `-0.3367` n `8`; equity avg `0.6286` n `108`; fx avg `-0.0266` n `6`; index avg `0.0954` n `25`; metal avg `0.0108` n `20`; unknown avg `0.1027` n `781`
- 24h: commodity avg `-1.3308` n `12`; crypto_alt avg `0.0448` n `230`; crypto_major avg `0.4816` n `8`; equity avg `3.6542` n `107`; fx avg `0.0508` n `6`; index avg `0.8057` n `25`; metal avg `0.8208` n `20`; unknown avg `0.4145` n `764`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
