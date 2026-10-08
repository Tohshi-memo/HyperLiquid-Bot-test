# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T06:23:07.036079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0195` n `13`; crypto_alt avg `-0.2639` n `235`; crypto_major avg `-0.2265` n `8`; equity avg `-0.2203` n `150`; fx avg `-0.0036` n `6`; index avg `-0.0402` n `26`; metal avg `-0.0249` n `20`; unknown avg `0.0471` n `1071`
- 1h: commodity avg `0.0244` n `13`; crypto_alt avg `-0.5997` n `235`; crypto_major avg `-0.4127` n `8`; equity avg `-0.5481` n `150`; fx avg `-0.0304` n `6`; index avg `-0.1137` n `26`; metal avg `-0.154` n `20`; unknown avg `0.255` n `1047`
- 4h: commodity avg `0.1047` n `13`; crypto_alt avg `-0.9544` n `235`; crypto_major avg `-0.9775` n `8`; equity avg `-0.9231` n `150`; fx avg `-0.0106` n `6`; index avg `-0.1495` n `26`; metal avg `-0.2418` n `20`; unknown avg `0.72` n `1041`
- 24h: commodity avg `0.3744` n `13`; crypto_alt avg `-1.3166` n `235`; crypto_major avg `-2.4401` n `8`; equity avg `-1.7098` n `150`; fx avg `-0.1522` n `6`; index avg `-0.2826` n `26`; metal avg `-0.2562` n `20`; unknown avg `416.6775` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
