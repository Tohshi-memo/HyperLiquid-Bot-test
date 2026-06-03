# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T15:07:34.497760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0253` n `12`; crypto_alt avg `-0.2005` n `228`; crypto_major avg `-0.2865` n `8`; equity avg `-0.2702` n `73`; fx avg `0.0197` n `6`; index avg `-0.0632` n `23`; metal avg `-0.1099` n `18`; unknown avg `1.0746` n `419`
- 1h: commodity avg `0.3322` n `12`; crypto_alt avg `0.0216` n `228`; crypto_major avg `-0.2422` n `8`; equity avg `0.0682` n `73`; fx avg `0.0233` n `6`; index avg `0.1131` n `23`; metal avg `-0.0746` n `18`; unknown avg `0.9347` n `419`
- 4h: commodity avg `-0.5336` n `12`; crypto_alt avg `-0.1932` n `228`; crypto_major avg `-1.174` n `8`; equity avg `-1.5668` n `73`; fx avg `-0.0155` n `6`; index avg `-0.4301` n `23`; metal avg `-0.8263` n `18`; unknown avg `0.7768` n `419`
- 24h: commodity avg `1.2844` n `12`; crypto_alt avg `1.3305` n `228`; crypto_major avg `-2.3153` n `8`; equity avg `-0.9772` n `72`; fx avg `0.0345` n `6`; index avg `0.0514` n `23`; metal avg `-1.812` n `18`; unknown avg `0.3656` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
