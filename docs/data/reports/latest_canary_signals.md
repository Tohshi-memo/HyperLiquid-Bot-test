# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T04:37:27.739458+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1684` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0206` n `13`; crypto_alt avg `0.1328` n `239`; crypto_major avg `0.0743` n `8`; equity avg `0.044` n `166`; fx avg `-0.016` n `6`; index avg `0.0018` n `27`; metal avg `0.0142` n `20`; unknown avg `158.9102` n `1259`
- 1h: commodity avg `0.0095` n `13`; crypto_alt avg `0.3727` n `239`; crypto_major avg `0.2147` n `8`; equity avg `-0.0286` n `166`; fx avg `-0.0161` n `6`; index avg `0.0139` n `27`; metal avg `0.0288` n `20`; unknown avg `325.0565` n `1255`
- 4h: commodity avg `-0.0919` n `13`; crypto_alt avg `-0.7771` n `239`; crypto_major avg `-1.2537` n `8`; equity avg `-0.4906` n `166`; fx avg `-0.022` n `6`; index avg `-0.0853` n `27`; metal avg `-0.0941` n `20`; unknown avg `9.0386` n `1255`
- 24h: commodity avg `0.0015` n `13`; crypto_alt avg `3.3715` n `239`; crypto_major avg `5.3494` n `8`; equity avg `1.7911` n `166`; fx avg `-0.039` n `6`; index avg `0.2117` n `27`; metal avg `0.2133` n `20`; unknown avg `836.819` n `1078`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
