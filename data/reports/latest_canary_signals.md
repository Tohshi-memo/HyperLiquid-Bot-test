# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T08:37:22.930951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.12` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.9229` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0614` n `12`; crypto_alt avg `0.1849` n `228`; crypto_major avg `0.0736` n `8`; equity avg `-0.022` n `72`; fx avg `0.0084` n `6`; index avg `-0.0133` n `23`; metal avg `0.1284` n `18`; unknown avg `0.3518` n `420`
- 1h: commodity avg `0.2841` n `12`; crypto_alt avg `-0.1021` n `228`; crypto_major avg `-0.2577` n `8`; equity avg `-0.0722` n `72`; fx avg `-0.027` n `6`; index avg `-0.013` n `23`; metal avg `-0.016` n `18`; unknown avg `1.3188` n `420`
- 4h: commodity avg `0.654` n `12`; crypto_alt avg `2.3704` n `228`; crypto_major avg `1.4178` n `8`; equity avg `0.0171` n `72`; fx avg `0.0449` n `6`; index avg `-0.0789` n `23`; metal avg `-0.5051` n `18`; unknown avg `1.054` n `410`
- 24h: commodity avg `1.7415` n `12`; crypto_alt avg `-1.1097` n `228`; crypto_major avg `-3.56` n `8`; equity avg `0.5112` n `72`; fx avg `0.0264` n `6`; index avg `0.8036` n `23`; metal avg `-1.7441` n `18`; unknown avg `0.6791` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
