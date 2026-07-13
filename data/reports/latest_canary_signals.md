# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T06:07:25.406034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `12`; crypto_alt avg `0.0709` n `230`; crypto_major avg `0.0374` n `8`; equity avg `-0.1405` n `92`; fx avg `0.0145` n `6`; index avg `-0.0475` n `25`; metal avg `-0.0619` n `20`; unknown avg `-0.0642` n `750`
- 1h: commodity avg `0.0327` n `12`; crypto_alt avg `0.197` n `230`; crypto_major avg `0.0463` n `8`; equity avg `-0.0469` n `92`; fx avg `0.0437` n `6`; index avg `-0.0314` n `25`; metal avg `-0.1071` n `20`; unknown avg `-0.1037` n `750`
- 4h: commodity avg `0.0929` n `12`; crypto_alt avg `-0.0284` n `230`; crypto_major avg `-0.5548` n `8`; equity avg `-0.4877` n `92`; fx avg `0.0501` n `6`; index avg `-0.1056` n `25`; metal avg `-0.2022` n `20`; unknown avg `-0.1693` n `750`
- 24h: commodity avg `0.2555` n `12`; crypto_alt avg `-1.1625` n `230`; crypto_major avg `-0.8023` n `8`; equity avg `-2.2764` n `92`; fx avg `0.0695` n `6`; index avg `-0.5238` n `25`; metal avg `-0.5204` n `20`; unknown avg `-0.1191` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1852`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1763`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
