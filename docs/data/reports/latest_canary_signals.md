# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T20:07:38.610049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0135` n `13`; crypto_alt avg `0.0362` n `239`; crypto_major avg `-0.0327` n `8`; equity avg `0.0063` n `166`; fx avg `-0.0001` n `6`; index avg `-0.0016` n `27`; metal avg `-0.0351` n `20`; unknown avg `160.7311` n `1246`
- 1h: commodity avg `0.0363` n `13`; crypto_alt avg `-0.0327` n `239`; crypto_major avg `0.0139` n `8`; equity avg `0.004` n `166`; fx avg `-0.0017` n `6`; index avg `0.0156` n `27`; metal avg `0.0015` n `20`; unknown avg `0.529` n `1244`
- 4h: commodity avg `0.1007` n `13`; crypto_alt avg `-0.0309` n `239`; crypto_major avg `0.7104` n `8`; equity avg `0.1071` n `166`; fx avg `0.017` n `6`; index avg `0.0464` n `27`; metal avg `0.0517` n `20`; unknown avg `383.8288` n `1206`
- 24h: commodity avg `0.2027` n `13`; crypto_alt avg `1.5696` n `239`; crypto_major avg `3.1301` n `8`; equity avg `1.7697` n `166`; fx avg `-0.0695` n `6`; index avg `0.238` n `27`; metal avg `0.335` n `20`; unknown avg `131.6142` n `1090`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
