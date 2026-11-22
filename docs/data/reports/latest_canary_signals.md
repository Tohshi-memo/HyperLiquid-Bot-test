# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T01:37:27.542446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0343` n `13`; crypto_alt avg `-0.0313` n `239`; crypto_major avg `-0.1319` n `8`; equity avg `-0.0605` n `166`; fx avg `-0.0072` n `6`; index avg `0.0008` n `27`; metal avg `-0.0109` n `20`; unknown avg `1.2797` n `1263`
- 1h: commodity avg `-0.0113` n `13`; crypto_alt avg `-0.1412` n `239`; crypto_major avg `-0.1344` n `8`; equity avg `-0.0551` n `166`; fx avg `-0.0152` n `6`; index avg `-0.0018` n `27`; metal avg `0.0068` n `20`; unknown avg `203.7933` n `1263`
- 4h: commodity avg `-0.0243` n `13`; crypto_alt avg `0.0609` n `239`; crypto_major avg `-0.1801` n `8`; equity avg `0.069` n `166`; fx avg `0.0059` n `6`; index avg `0.0368` n `27`; metal avg `-0.0303` n `20`; unknown avg `163.9909` n `1232`
- 24h: commodity avg `0.0498` n `13`; crypto_alt avg `0.5606` n `239`; crypto_major avg `2.0136` n `8`; equity avg `0.6573` n `166`; fx avg `-0.0595` n `6`; index avg `0.181` n `27`; metal avg `0.1169` n `20`; unknown avg `232.9822` n `1080`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
