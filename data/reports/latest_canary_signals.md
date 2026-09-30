# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T06:22:29.758604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.05` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0195` n `12`; crypto_alt avg `-0.3049` n `234`; crypto_major avg `-0.2856` n `8`; equity avg `-0.0424` n `142`; fx avg `-0.0156` n `6`; index avg `0.0053` n `26`; metal avg `0.0068` n `20`; unknown avg `0.4575` n `961`
- 1h: commodity avg `-0.0991` n `12`; crypto_alt avg `-0.0863` n `234`; crypto_major avg `-0.0969` n `8`; equity avg `0.019` n `142`; fx avg `0.0313` n `6`; index avg `0.0223` n `26`; metal avg `0.097` n `20`; unknown avg `0.8631` n `931`
- 4h: commodity avg `-0.0022` n `12`; crypto_alt avg `0.1028` n `234`; crypto_major avg `-0.2455` n `8`; equity avg `-0.0675` n `142`; fx avg `0.0923` n `6`; index avg `0.0182` n `26`; metal avg `0.0473` n `20`; unknown avg `0.99` n `925`
- 24h: commodity avg `-0.9775` n `12`; crypto_alt avg `0.6938` n `234`; crypto_major avg `-0.7663` n `8`; equity avg `0.5656` n `142`; fx avg `-0.084` n `6`; index avg `0.1132` n `26`; metal avg `0.2224` n `20`; unknown avg `2857.6464` n `824`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1726`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
