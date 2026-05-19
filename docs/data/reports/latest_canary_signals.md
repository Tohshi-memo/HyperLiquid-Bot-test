# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T08:37:21.026336+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `0.0781` n `228`; crypto_major avg `-0.0463` n `8`; equity avg `-0.1247` n `66`; fx avg `-0.0105` n `6`; index avg `-0.0521` n `23`; metal avg `-0.0121` n `18`; unknown avg `0.0596` n `383`
- 1h: commodity avg `-0.0453` n `12`; crypto_alt avg `-0.243` n `228`; crypto_major avg `-0.2359` n `8`; equity avg `-0.2458` n `66`; fx avg `-0.0173` n `6`; index avg `-0.1135` n `23`; metal avg `0.0021` n `18`; unknown avg `-0.0119` n `383`
- 4h: commodity avg `0.2835` n `12`; crypto_alt avg `0.0254` n `228`; crypto_major avg `0.1247` n `8`; equity avg `0.1813` n `66`; fx avg `-0.0089` n `6`; index avg `0.136` n `23`; metal avg `-0.0381` n `18`; unknown avg `0.0566` n `363`
- 24h: commodity avg `0.6753` n `12`; crypto_alt avg `1.7737` n `228`; crypto_major avg `0.9619` n `8`; equity avg `-1.4349` n `66`; fx avg `0.3168` n `6`; index avg `-0.6284` n `23`; metal avg `-0.2406` n `18`; unknown avg `1.0285` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
