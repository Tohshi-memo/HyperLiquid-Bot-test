# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T11:22:30.691462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1012` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0249` n `13`; crypto_alt avg `-0.2588` n `239`; crypto_major avg `-0.1059` n `8`; equity avg `-0.1967` n `166`; fx avg `0.0078` n `6`; index avg `-0.0224` n `27`; metal avg `0.0205` n `20`; unknown avg `0.1351` n `1264`
- 1h: commodity avg `-0.0304` n `13`; crypto_alt avg `-0.7117` n `239`; crypto_major avg `-0.4834` n `8`; equity avg `-0.8947` n `166`; fx avg `0.0031` n `6`; index avg `-0.1198` n `27`; metal avg `0.0605` n `20`; unknown avg `0.169` n `1262`
- 4h: commodity avg `0.0886` n `13`; crypto_alt avg `-2.0974` n `239`; crypto_major avg `-1.4299` n `8`; equity avg `-2.6142` n `166`; fx avg `0.0811` n `6`; index avg `-0.3287` n `27`; metal avg `-0.1435` n `20`; unknown avg `0.5136` n `1200`
- 24h: commodity avg `-0.4171` n `13`; crypto_alt avg `-1.6618` n `239`; crypto_major avg `-1.791` n `8`; equity avg `0.664` n `166`; fx avg `-0.0864` n `6`; index avg `0.2183` n `27`; metal avg `-0.3986` n `20`; unknown avg `0.1889` n `1138`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
