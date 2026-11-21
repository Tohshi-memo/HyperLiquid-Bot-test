# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T23:07:36.588564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0164` n `13`; crypto_alt avg `0.044` n `239`; crypto_major avg `0.0314` n `8`; equity avg `-0.0229` n `166`; fx avg `0.0067` n `6`; index avg `0.0013` n `27`; metal avg `0.0122` n `20`; unknown avg `160.3254` n `1246`
- 1h: commodity avg `-0.0179` n `13`; crypto_alt avg `0.2021` n `239`; crypto_major avg `0.0192` n `8`; equity avg `-0.0028` n `166`; fx avg `0.0177` n `6`; index avg `0.0031` n `27`; metal avg `-0.0063` n `20`; unknown avg `605.1375` n `1244`
- 4h: commodity avg `0.0066` n `13`; crypto_alt avg `-0.1713` n `239`; crypto_major avg `-0.3815` n `8`; equity avg `0.0718` n `166`; fx avg `0.0174` n `6`; index avg `0.0291` n `27`; metal avg `-0.0568` n `20`; unknown avg `-0.3167` n `1188`
- 24h: commodity avg `-0.0038` n `13`; crypto_alt avg `-0.4388` n `239`; crypto_major avg `1.1962` n `8`; equity avg `0.2993` n `166`; fx avg `-0.0363` n `6`; index avg `0.1274` n `27`; metal avg `0.0919` n `20`; unknown avg `239.189` n `1078`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
