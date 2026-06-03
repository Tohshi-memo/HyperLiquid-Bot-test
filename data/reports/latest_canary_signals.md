# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T16:37:24.790899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2729` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0888` n `12`; crypto_alt avg `0.1717` n `228`; crypto_major avg `0.2443` n `8`; equity avg `-0.2674` n `73`; fx avg `-0.0011` n `6`; index avg `-0.04` n `23`; metal avg `-0.044` n `18`; unknown avg `-0.1637` n `419`
- 1h: commodity avg `0.1024` n `12`; crypto_alt avg `-1.0987` n `228`; crypto_major avg `-0.8676` n `8`; equity avg `-0.5597` n `73`; fx avg `-0.0207` n `6`; index avg `-0.0889` n `23`; metal avg `-0.2197` n `18`; unknown avg `-0.2513` n `419`
- 4h: commodity avg `-0.0794` n `12`; crypto_alt avg `-1.2059` n `228`; crypto_major avg `-1.8453` n `8`; equity avg `-2.2487` n `73`; fx avg `-0.0295` n `6`; index avg `-0.5724` n `23`; metal avg `-0.7749` n `18`; unknown avg `-0.1005` n `419`
- 24h: commodity avg `1.0394` n `12`; crypto_alt avg `-0.26` n `228`; crypto_major avg `-3.2484` n `8`; equity avg `-2.164` n `72`; fx avg `0.0113` n `6`; index avg `-0.3002` n `23`; metal avg `-2.0075` n `18`; unknown avg `-0.0771` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
