# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T00:07:26.542751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `13`; crypto_alt avg `-0.0642` n `239`; crypto_major avg `0.0186` n `8`; equity avg `0.0492` n `166`; fx avg `0.009` n `6`; index avg `0.0007` n `27`; metal avg `0.0053` n `20`; unknown avg `16.2836` n `1251`
- 1h: commodity avg `0.0128` n `13`; crypto_alt avg `0.1585` n `239`; crypto_major avg `0.2172` n `8`; equity avg `0.1286` n `166`; fx avg `-0.0046` n `6`; index avg `0.0265` n `27`; metal avg `0.0131` n `20`; unknown avg `107.8525` n `1254`
- 4h: commodity avg `-0.0169` n `13`; crypto_alt avg `0.0216` n `239`; crypto_major avg `-0.1791` n `8`; equity avg `0.1968` n `166`; fx avg `0.0145` n `6`; index avg `0.0401` n `27`; metal avg `-0.0451` n `20`; unknown avg `0.1588` n `1196`
- 24h: commodity avg `0.062` n `13`; crypto_alt avg `0.2978` n `239`; crypto_major avg `1.7843` n `8`; equity avg `0.7291` n `166`; fx avg `-0.0314` n `6`; index avg `0.172` n `27`; metal avg `0.1206` n `20`; unknown avg `233.0448` n `1080`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
