# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T05:52:25.777538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.3` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1447` n `12`; crypto_alt avg `0.2791` n `228`; crypto_major avg `0.2467` n `8`; equity avg `-0.0488` n `72`; fx avg `0.0145` n `6`; index avg `-0.0078` n `23`; metal avg `-0.046` n `18`; unknown avg `-0.1968` n `420`
- 1h: commodity avg `0.0386` n `12`; crypto_alt avg `1.3726` n `228`; crypto_major avg `0.9873` n `8`; equity avg `-0.0046` n `72`; fx avg `0.052` n `6`; index avg `-0.0541` n `23`; metal avg `-0.2071` n `18`; unknown avg `0.0588` n `420`
- 4h: commodity avg `0.1236` n `12`; crypto_alt avg `1.6739` n `228`; crypto_major avg `0.9668` n `8`; equity avg `0.3174` n `72`; fx avg `0.0732` n `6`; index avg `0.0279` n `23`; metal avg `-0.1449` n `18`; unknown avg `0.0745` n `419`
- 24h: commodity avg `1.1179` n `12`; crypto_alt avg `-1.895` n `228`; crypto_major avg `-4.0223` n `8`; equity avg `0.8868` n `72`; fx avg `0.0856` n `6`; index avg `1.052` n `23`; metal avg `-1.1732` n `18`; unknown avg `-0.8389` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
