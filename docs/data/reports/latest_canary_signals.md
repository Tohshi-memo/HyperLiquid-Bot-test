# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T16:22:26.678274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.023` n `12`; crypto_alt avg `0.0753` n `229`; crypto_major avg `0.1339` n `8`; equity avg `0.3897` n `91`; fx avg `-0.0124` n `6`; index avg `0.0624` n `25`; metal avg `0.0876` n `20`; unknown avg `0.3235` n `763`
- 1h: commodity avg `0.0143` n `12`; crypto_alt avg `0.4415` n `229`; crypto_major avg `0.3767` n `8`; equity avg `0.862` n `91`; fx avg `-0.0346` n `6`; index avg `0.1623` n `25`; metal avg `0.1139` n `20`; unknown avg `0.3012` n `755`
- 4h: commodity avg `0.5155` n `12`; crypto_alt avg `-0.2549` n `229`; crypto_major avg `0.1869` n `8`; equity avg `-1.1158` n `91`; fx avg `-0.0253` n `6`; index avg `-0.1395` n `25`; metal avg `-0.2266` n `20`; unknown avg `0.1799` n `755`
- 24h: commodity avg `0.5722` n `12`; crypto_alt avg `-0.7174` n `229`; crypto_major avg `-0.1056` n `8`; equity avg `-3.0873` n `91`; fx avg `-0.2494` n `6`; index avg `-0.6026` n `25`; metal avg `0.0465` n `20`; unknown avg `0.2119` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
