# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T17:52:31.046228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `13`; crypto_alt avg `0.0315` n `239`; crypto_major avg `-0.0446` n `8`; equity avg `0.0084` n `166`; fx avg `-0.0001` n `6`; index avg `-0.009` n `27`; metal avg `0.0043` n `20`; unknown avg `1.0187` n `1262`
- 1h: commodity avg `0.0265` n `13`; crypto_alt avg `0.1884` n `239`; crypto_major avg `0.0736` n `8`; equity avg `-0.0121` n `166`; fx avg `0.0063` n `6`; index avg `-0.001` n `27`; metal avg `0.0182` n `20`; unknown avg `0.431` n `1252`
- 4h: commodity avg `-0.0005` n `13`; crypto_alt avg `-0.154` n `239`; crypto_major avg `-0.3654` n `8`; equity avg `-0.1762` n `166`; fx avg `0.0023` n `6`; index avg `-0.0368` n `27`; metal avg `-0.0266` n `20`; unknown avg `165.387` n `1240`
- 24h: commodity avg `0.4585` n `13`; crypto_alt avg `1.184` n `239`; crypto_major avg `1.8033` n `8`; equity avg `0.2161` n `166`; fx avg `-0.1078` n `6`; index avg `0.0027` n `27`; metal avg `0.2164` n `20`; unknown avg `0.6758` n `1134`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
