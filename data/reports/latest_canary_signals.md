# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T23:37:29.982487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `13`; crypto_alt avg `0.0476` n `239`; crypto_major avg `-0.0023` n `8`; equity avg `-0.0399` n `166`; fx avg `-0.0061` n `6`; index avg `-0.005` n `27`; metal avg `0.0029` n `20`; unknown avg `318.9773` n `1262`
- 1h: commodity avg `-0.0018` n `13`; crypto_alt avg `0.1928` n `239`; crypto_major avg `-0.1137` n `8`; equity avg `0.3146` n `166`; fx avg `-0.0292` n `6`; index avg `0.0563` n `27`; metal avg `0.031` n `20`; unknown avg `2.3793` n `1246`
- 4h: commodity avg `0.2442` n `13`; crypto_alt avg `1.3401` n `239`; crypto_major avg `1.2588` n `8`; equity avg `0.9487` n `166`; fx avg `-0.0517` n `6`; index avg `0.0857` n `27`; metal avg `0.1516` n `20`; unknown avg `240.0527` n `1198`
- 24h: commodity avg `0.2703` n `13`; crypto_alt avg `-4.588` n `239`; crypto_major avg `-5.2958` n `8`; equity avg `-5.2568` n `166`; fx avg `-0.0186` n `6`; index avg `-0.5874` n `27`; metal avg `-0.57` n `20`; unknown avg `12.2725` n `1121`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
