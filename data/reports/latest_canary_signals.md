# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T12:22:30.209265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `13`; crypto_alt avg `-0.0767` n `234`; crypto_major avg `-0.0842` n `8`; equity avg `-0.0331` n `142`; fx avg `-0.0007` n `6`; index avg `-0.0035` n `26`; metal avg `0.013` n `20`; unknown avg `-0.0519` n `975`
- 1h: commodity avg `-0.0388` n `13`; crypto_alt avg `0.1101` n `234`; crypto_major avg `0.1956` n `8`; equity avg `-0.0463` n `142`; fx avg `-0.003` n `6`; index avg `0.0391` n `26`; metal avg `0.1818` n `20`; unknown avg `0.2604` n `967`
- 4h: commodity avg `-0.2067` n `13`; crypto_alt avg `-0.1451` n `234`; crypto_major avg `0.7073` n `8`; equity avg `0.1824` n `142`; fx avg `-0.0247` n `6`; index avg `0.1239` n `26`; metal avg `0.3064` n `20`; unknown avg `3.5207` n `967`
- 24h: commodity avg `-0.1722` n `13`; crypto_alt avg `-0.6355` n `234`; crypto_major avg `0.1936` n `8`; equity avg `0.5534` n `142`; fx avg `0.0502` n `6`; index avg `0.2164` n `26`; metal avg `0.0212` n `20`; unknown avg `773.1861` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
