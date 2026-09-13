# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T13:22:25.885868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0182` n `12`; crypto_alt avg `-0.1105` n `233`; crypto_major avg `-0.152` n `8`; equity avg `-0.0292` n `136`; fx avg `0.0015` n `6`; index avg `0.006` n `27`; metal avg `0.0022` n `20`; unknown avg `0.1932` n `838`
- 1h: commodity avg `0.0192` n `12`; crypto_alt avg `-0.2202` n `233`; crypto_major avg `-0.2703` n `8`; equity avg `-0.1219` n `136`; fx avg `-0.0006` n `6`; index avg `-0.0054` n `27`; metal avg `0.0026` n `20`; unknown avg `0.152` n `830`
- 4h: commodity avg `0.1812` n `12`; crypto_alt avg `-0.5351` n `233`; crypto_major avg `-0.949` n `8`; equity avg `-0.8183` n `136`; fx avg `0.0078` n `6`; index avg `-0.1367` n `27`; metal avg `-0.0461` n `20`; unknown avg `0.4478` n `826`
- 24h: commodity avg `0.2748` n `12`; crypto_alt avg `-0.612` n `233`; crypto_major avg `-2.0584` n `8`; equity avg `-1.9195` n `136`; fx avg `-0.0054` n `6`; index avg `-0.3061` n `26`; metal avg `-0.0751` n `20`; unknown avg `-0.0736` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
