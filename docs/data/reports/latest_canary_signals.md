# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T22:07:18.169507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0805` n `12`; crypto_alt avg `0.2547` n `228`; crypto_major avg `-0.0299` n `8`; equity avg `0.0541` n `66`; fx avg `-0.0002` n `6`; index avg `-0.0393` n `23`; metal avg `0.0313` n `18`; unknown avg `-0.003` n `383`
- 1h: commodity avg `-0.1627` n `12`; crypto_alt avg `1.0531` n `228`; crypto_major avg `0.7704` n `8`; equity avg `0.365` n `66`; fx avg `-0.0179` n `6`; index avg `0.2273` n `23`; metal avg `0.0607` n `18`; unknown avg `0.2004` n `383`
- 4h: commodity avg `-0.4279` n `12`; crypto_alt avg `1.9375` n `228`; crypto_major avg `1.4013` n `8`; equity avg `0.8705` n `66`; fx avg `-0.044` n `6`; index avg `0.5668` n `23`; metal avg `0.5834` n `18`; unknown avg `0.7401` n `383`
- 24h: commodity avg `0.8743` n `12`; crypto_alt avg `-1.1027` n `228`; crypto_major avg `-1.6464` n `8`; equity avg `-0.7949` n `66`; fx avg `0.1743` n `6`; index avg `-0.2668` n `23`; metal avg `0.6381` n `18`; unknown avg `-0.158` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
