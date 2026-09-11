# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T11:33:43.176679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.05` n `12`; crypto_alt avg `0.1787` n `233`; crypto_major avg `0.0872` n `8`; equity avg `0.0631` n `136`; fx avg `-0.0028` n `6`; index avg `0.0201` n `26`; metal avg `-0.0079` n `20`; unknown avg `0.1035` n `796`
- 1h: commodity avg `0.0797` n `12`; crypto_alt avg `-0.476` n `233`; crypto_major avg `-0.4149` n `8`; equity avg `-0.1484` n `136`; fx avg `-0.0152` n `6`; index avg `-0.0064` n `26`; metal avg `-0.0847` n `20`; unknown avg `0.0051` n `794`
- 4h: commodity avg `-0.2966` n `12`; crypto_alt avg `-1.4468` n `233`; crypto_major avg `-0.8761` n `8`; equity avg `0.0343` n `136`; fx avg `-0.0855` n `6`; index avg `0.0602` n `26`; metal avg `-0.0471` n `20`; unknown avg `-0.2127` n `788`
- 24h: commodity avg `0.3494` n `12`; crypto_alt avg `-2.499` n `233`; crypto_major avg `-2.111` n `8`; equity avg `-0.9455` n `136`; fx avg `-0.1044` n `6`; index avg `-0.0953` n `26`; metal avg `-0.4972` n `20`; unknown avg `1.0379` n `683`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
