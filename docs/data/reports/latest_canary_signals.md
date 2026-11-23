# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T21:22:35.426160+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7473` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5612` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0218` n `13`; crypto_alt avg `-0.343` n `239`; crypto_major avg `-0.319` n `8`; equity avg `-0.1987` n `166`; fx avg `-0.0072` n `6`; index avg `-0.0316` n `27`; metal avg `-0.022` n `20`; unknown avg `0.6225` n `1254`
- 1h: commodity avg `0.0898` n `13`; crypto_alt avg `-0.6658` n `239`; crypto_major avg `-0.455` n `8`; equity avg `-0.0482` n `166`; fx avg `-0.0069` n `6`; index avg `-0.0122` n `27`; metal avg `-0.0431` n `20`; unknown avg `162.3694` n `1236`
- 4h: commodity avg `-0.1243` n `13`; crypto_alt avg `-1.9399` n `239`; crypto_major avg `-1.7751` n `8`; equity avg `-0.3334` n `166`; fx avg `-0.0222` n `6`; index avg `-0.0278` n `27`; metal avg `-0.2139` n `20`; unknown avg `164.3895` n `1230`
- 24h: commodity avg `-1.4521` n `13`; crypto_alt avg `0.7577` n `239`; crypto_major avg `1.1131` n `8`; equity avg `5.8405` n `166`; fx avg `-0.086` n `6`; index avg `0.573` n `27`; metal avg `0.6134` n `20`; unknown avg `241.817` n `1052`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
