# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T10:43:24.580586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5839` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0044` n `13`; crypto_alt avg `0.0386` n `239`; crypto_major avg `-0.0691` n `8`; equity avg `-0.0217` n `162`; fx avg `-0.0036` n `6`; index avg `0.0004` n `27`; metal avg `-0.0125` n `20`; unknown avg `-0.0774` n `1261`
- 1h: commodity avg `-0.0318` n `13`; crypto_alt avg `0.3772` n `239`; crypto_major avg `0.3533` n `8`; equity avg `-0.0402` n `162`; fx avg `-0.0035` n `6`; index avg `-0.0019` n `27`; metal avg `0.0024` n `20`; unknown avg `-0.0113` n `1257`
- 4h: commodity avg `-0.0647` n `13`; crypto_alt avg `0.9204` n `239`; crypto_major avg `1.7526` n `8`; equity avg `0.3658` n `162`; fx avg `-0.0202` n `6`; index avg `0.0404` n `27`; metal avg `0.1687` n `20`; unknown avg `0.7453` n `1241`
- 24h: commodity avg `0.0074` n `13`; crypto_alt avg `-3.7634` n `239`; crypto_major avg `-3.2066` n `8`; equity avg `-0.7425` n `162`; fx avg `0.0286` n `6`; index avg `-0.06` n `27`; metal avg `-0.3476` n `20`; unknown avg `-0.1351` n `1136`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
