# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T08:37:30.519637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0796` n `12`; crypto_alt avg `0.0357` n `230`; crypto_major avg `0.1668` n `8`; equity avg `0.1421` n `92`; fx avg `0.0104` n `6`; index avg `0.0254` n `25`; metal avg `0.0183` n `20`; unknown avg `0.0115` n `766`
- 1h: commodity avg `-0.0539` n `12`; crypto_alt avg `-0.0246` n `230`; crypto_major avg `0.2086` n `8`; equity avg `0.2191` n `92`; fx avg `0.0297` n `6`; index avg `0.0085` n `25`; metal avg `-0.0452` n `20`; unknown avg `-0.0163` n `766`
- 4h: commodity avg `0.1437` n `12`; crypto_alt avg `0.146` n `230`; crypto_major avg `0.1051` n `8`; equity avg `1.0304` n `92`; fx avg `0.0953` n `6`; index avg `0.1759` n `25`; metal avg `0.0406` n `20`; unknown avg `0.0915` n `750`
- 24h: commodity avg `1.3884` n `12`; crypto_alt avg `-0.6819` n `230`; crypto_major avg `-0.6575` n `8`; equity avg `-0.3022` n `92`; fx avg `-0.0929` n `6`; index avg `-0.0993` n `25`; metal avg `-0.1792` n `20`; unknown avg `-0.2211` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1815`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
