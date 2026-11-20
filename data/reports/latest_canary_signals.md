# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T23:07:24.966666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.24` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0112` n `13`; crypto_alt avg `0.3719` n `239`; crypto_major avg `0.2816` n `8`; equity avg `0.2873` n `166`; fx avg `0.0118` n `6`; index avg `0.0312` n `27`; metal avg `0.0279` n `20`; unknown avg `11.6333` n `1252`
- 1h: commodity avg `-0.0148` n `13`; crypto_alt avg `0.5853` n `239`; crypto_major avg `0.3039` n `8`; equity avg `0.7879` n `166`; fx avg `-0.0285` n `6`; index avg `0.078` n `27`; metal avg `0.0249` n `20`; unknown avg `0.1766` n `1244`
- 4h: commodity avg `0.2862` n `13`; crypto_alt avg `1.1321` n `239`; crypto_major avg `0.9416` n `8`; equity avg `-0.0973` n `166`; fx avg `-0.0322` n `6`; index avg `-0.0674` n `27`; metal avg `-0.0037` n `20`; unknown avg `55.376` n `1200`
- 24h: commodity avg `0.2614` n `13`; crypto_alt avg `-4.4037` n `239`; crypto_major avg `-5.3674` n `8`; equity avg `-5.7593` n `166`; fx avg `0.0071` n `6`; index avg `-0.6415` n `27`; metal avg `-0.7897` n `20`; unknown avg `38.1273` n `1121`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
