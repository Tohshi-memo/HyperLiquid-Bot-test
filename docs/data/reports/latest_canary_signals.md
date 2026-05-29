# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T22:07:21.666639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1058` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0357` n `12`; crypto_alt avg `-0.3527` n `228`; crypto_major avg `-0.1133` n `8`; equity avg `-0.0174` n `69`; fx avg `0.0036` n `6`; index avg `0.011` n `23`; metal avg `0.0106` n `18`; unknown avg `0.7365` n `419`
- 1h: commodity avg `-0.1861` n `12`; crypto_alt avg `-0.735` n `228`; crypto_major avg `-0.5327` n `8`; equity avg `-0.0928` n `69`; fx avg `-0.0115` n `6`; index avg `0.0327` n `23`; metal avg `0.0389` n `18`; unknown avg `1.0895` n `419`
- 4h: commodity avg `0.1341` n `12`; crypto_alt avg `-1.3655` n `228`; crypto_major avg `-1.0185` n `8`; equity avg `0.0853` n `69`; fx avg `-0.0147` n `6`; index avg `0.0873` n `23`; metal avg `-0.1548` n `18`; unknown avg `-0.1882` n `419`
- 24h: commodity avg `-0.5659` n `12`; crypto_alt avg `-0.1547` n `228`; crypto_major avg `0.2751` n `8`; equity avg `0.9675` n `69`; fx avg `0.1837` n `6`; index avg `0.1139` n `23`; metal avg `-0.0624` n `18`; unknown avg `1.0889` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1893`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
