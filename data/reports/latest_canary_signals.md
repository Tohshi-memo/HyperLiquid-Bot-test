# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T22:22:27.179377+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.15` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.003` n `12`; crypto_alt avg `0.2149` n `233`; crypto_major avg `0.1477` n `8`; equity avg `0.0252` n `136`; fx avg `0.0022` n `6`; index avg `0.001` n `26`; metal avg `-0.001` n `20`; unknown avg `2.1216` n `830`
- 1h: commodity avg `-0.0176` n `12`; crypto_alt avg `-0.6791` n `233`; crypto_major avg `-0.5111` n `8`; equity avg `-0.0199` n `136`; fx avg `-0.0149` n `6`; index avg `0.0058` n `26`; metal avg `-0.0124` n `20`; unknown avg `3.6879` n `820`
- 4h: commodity avg `-0.1113` n `12`; crypto_alt avg `-0.5843` n `233`; crypto_major avg `-0.2153` n `8`; equity avg `-0.1983` n `136`; fx avg `-0.0081` n `6`; index avg `-0.0191` n `26`; metal avg `0.016` n `20`; unknown avg `1.0586` n `770`
- 24h: commodity avg `-0.7981` n `12`; crypto_alt avg `-0.2064` n `233`; crypto_major avg `0.73` n `8`; equity avg `0.6961` n `136`; fx avg `-0.1977` n `6`; index avg `0.3081` n `26`; metal avg `0.2706` n `20`; unknown avg `1.7179` n `684`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
