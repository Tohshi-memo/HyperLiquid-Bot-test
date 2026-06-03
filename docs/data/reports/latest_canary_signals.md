# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T04:52:24.329380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.51` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0655` n `12`; crypto_alt avg `0.2861` n `228`; crypto_major avg `0.3083` n `8`; equity avg `0.0489` n `72`; fx avg `-0.0067` n `6`; index avg `-0.0508` n `23`; metal avg `-0.0083` n `18`; unknown avg `0.9363` n `420`
- 1h: commodity avg `0.1793` n `12`; crypto_alt avg `1.4495` n `228`; crypto_major avg `1.1331` n `8`; equity avg `0.2596` n `72`; fx avg `-0.0074` n `6`; index avg `-0.0265` n `23`; metal avg `-0.2265` n `18`; unknown avg `-0.2013` n `420`
- 4h: commodity avg `0.2029` n `12`; crypto_alt avg `0.0571` n `228`; crypto_major avg `-0.5679` n `8`; equity avg `0.0039` n `72`; fx avg `0.0035` n `6`; index avg `0.0052` n `23`; metal avg `-0.369` n `18`; unknown avg `0.3309` n `419`
- 24h: commodity avg `1.0002` n `12`; crypto_alt avg `-3.8398` n `228`; crypto_major avg `-5.6369` n `8`; equity avg `1.1481` n `72`; fx avg `0.0382` n `6`; index avg `1.3618` n `23`; metal avg `-0.5093` n `18`; unknown avg `0.271` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
