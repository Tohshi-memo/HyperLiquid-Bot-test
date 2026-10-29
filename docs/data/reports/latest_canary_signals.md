# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T16:52:35.920496+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.8721` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0444` n `13`; crypto_alt avg `-0.0945` n `238`; crypto_major avg `-0.0719` n `8`; equity avg `-0.073` n `156`; fx avg `0.0028` n `6`; index avg `0.0014` n `27`; metal avg `0.0002` n `20`; unknown avg `0.6524` n `1238`
- 1h: commodity avg `0.0979` n `13`; crypto_alt avg `-0.2691` n `238`; crypto_major avg `-0.093` n `8`; equity avg `-0.306` n `156`; fx avg `-0.0024` n `6`; index avg `-0.0223` n `27`; metal avg `-0.0345` n `20`; unknown avg `1.3493` n `1226`
- 4h: commodity avg `0.0597` n `13`; crypto_alt avg `1.6603` n `238`; crypto_major avg `1.8539` n `8`; equity avg `0.5746` n `156`; fx avg `0.0993` n `6`; index avg `0.0079` n `27`; metal avg `-0.0182` n `20`; unknown avg `26.3356` n `1132`
- 24h: commodity avg `-0.6518` n `13`; crypto_alt avg `1.1717` n `238`; crypto_major avg `2.7232` n `8`; equity avg `-0.7092` n `155`; fx avg `0.0134` n `6`; index avg `-0.1685` n `27`; metal avg `-0.5329` n `20`; unknown avg `43.0862` n `946`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
