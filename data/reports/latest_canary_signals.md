# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T10:37:22.452911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.03` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1432` n `12`; crypto_alt avg `0.2667` n `228`; crypto_major avg `0.0746` n `8`; equity avg `-0.0141` n `72`; fx avg `0.0139` n `6`; index avg `-0.0227` n `23`; metal avg `-0.0398` n `18`; unknown avg `-0.0963` n `420`
- 1h: commodity avg `0.0189` n `12`; crypto_alt avg `0.7186` n `228`; crypto_major avg `0.4097` n `8`; equity avg `-0.0452` n `72`; fx avg `0.0069` n `6`; index avg `0.0054` n `23`; metal avg `0.2236` n `18`; unknown avg `-0.155` n `420`
- 4h: commodity avg `0.7754` n `12`; crypto_alt avg `0.3117` n `228`; crypto_major avg `-0.1055` n `8`; equity avg `-0.3668` n `72`; fx avg `-0.0092` n `6`; index avg `-0.0147` n `23`; metal avg `-0.0196` n `18`; unknown avg `-0.1026` n `420`
- 24h: commodity avg `1.8828` n `12`; crypto_alt avg `-0.5291` n `228`; crypto_major avg `-2.8199` n `8`; equity avg `0.578` n `72`; fx avg `0.059` n `6`; index avg `0.8133` n `23`; metal avg `-1.3176` n `18`; unknown avg `0.0249` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0444`, n `668`, weak_sample_signal
