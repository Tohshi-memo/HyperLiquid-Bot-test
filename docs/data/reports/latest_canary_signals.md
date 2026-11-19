# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T13:37:34.497849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0988` n `13`; crypto_alt avg `0.0289` n `239`; crypto_major avg `0.0599` n `8`; equity avg `-0.2784` n `164`; fx avg `0.0161` n `6`; index avg `-0.0445` n `27`; metal avg `0.0232` n `20`; unknown avg `0.1896` n `1266`
- 1h: commodity avg `0.1104` n `13`; crypto_alt avg `0.5776` n `239`; crypto_major avg `0.3801` n `8`; equity avg `-0.4025` n `164`; fx avg `0.0155` n `6`; index avg `-0.0472` n `27`; metal avg `-0.0104` n `20`; unknown avg `12.158` n `1264`
- 4h: commodity avg `0.3647` n `13`; crypto_alt avg `0.0231` n `239`; crypto_major avg `0.1545` n `8`; equity avg `-0.0085` n `164`; fx avg `-0.008` n `6`; index avg `0.0444` n `27`; metal avg `-0.1765` n `20`; unknown avg `104.33` n `1258`
- 24h: commodity avg `0.0155` n `13`; crypto_alt avg `0.2831` n `239`; crypto_major avg `0.2328` n `8`; equity avg `0.6793` n `164`; fx avg `0.0135` n `6`; index avg `0.2612` n `27`; metal avg `-0.3038` n `20`; unknown avg `2.2235` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
