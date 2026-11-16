# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T03:52:43.600951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0318` n `13`; crypto_alt avg `0.0496` n `239`; crypto_major avg `0.1625` n `8`; equity avg `-0.0746` n `162`; fx avg `-0.003` n `6`; index avg `0.0084` n `27`; metal avg `0.0576` n `20`; unknown avg `0.0816` n `1265`
- 1h: commodity avg `0.0632` n `13`; crypto_alt avg `-0.3937` n `239`; crypto_major avg `-0.1508` n `8`; equity avg `-0.2927` n `162`; fx avg `-0.0045` n `6`; index avg `-0.0259` n `27`; metal avg `0.0552` n `20`; unknown avg `0.111` n `1259`
- 4h: commodity avg `-0.0517` n `13`; crypto_alt avg `-0.6356` n `239`; crypto_major avg `-0.9241` n `8`; equity avg `-1.5952` n `162`; fx avg `-0.0268` n `6`; index avg `-0.2707` n `27`; metal avg `-0.4185` n `20`; unknown avg `1.8294` n `1239`
- 24h: commodity avg `-0.3856` n `13`; crypto_alt avg `-0.0387` n `239`; crypto_major avg `0.1457` n `8`; equity avg `0.0486` n `162`; fx avg `-0.0202` n `6`; index avg `0.0187` n `27`; metal avg `0.1918` n `20`; unknown avg `0.7775` n `1125`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
