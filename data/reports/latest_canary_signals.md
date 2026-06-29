# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T13:22:33.519257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.51` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0371` n `12`; crypto_alt avg `-0.1185` n `228`; crypto_major avg `-0.0351` n `8`; equity avg `-0.0394` n `88`; fx avg `0.0011` n `6`; index avg `-0.0152` n `23`; metal avg `-0.0416` n `20`; unknown avg `0.5984` n `764`
- 1h: commodity avg `-0.0955` n `12`; crypto_alt avg `-0.442` n `228`; crypto_major avg `-0.3404` n `8`; equity avg `-0.2006` n `88`; fx avg `0.0134` n `6`; index avg `-0.0241` n `23`; metal avg `0.0299` n `20`; unknown avg `0.4613` n `764`
- 4h: commodity avg `-0.1399` n `12`; crypto_alt avg `0.3901` n `228`; crypto_major avg `0.8098` n `8`; equity avg `0.1995` n `88`; fx avg `0.0624` n `6`; index avg `-0.0103` n `23`; metal avg `-0.0672` n `20`; unknown avg `0.5857` n `764`
- 24h: commodity avg `-0.6074` n `12`; crypto_alt avg `0.7234` n `228`; crypto_major avg `0.7378` n `8`; equity avg `0.5929` n `88`; fx avg `0.0856` n `6`; index avg `0.0422` n `23`; metal avg `-0.3595` n `20`; unknown avg `1.8313` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
