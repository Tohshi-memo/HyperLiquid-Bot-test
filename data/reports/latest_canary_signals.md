# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T00:12:43.899225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0753` n `12`; crypto_alt avg `-0.0215` n `234`; crypto_major avg `-0.0503` n `8`; equity avg `0.0193` n `142`; fx avg `0.047` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0371` n `20`; unknown avg `0.3487` n `951`
- 1h: commodity avg `0.0391` n `12`; crypto_alt avg `-0.0543` n `234`; crypto_major avg `-0.1756` n `8`; equity avg `0.0883` n `142`; fx avg `0.0548` n `6`; index avg `0.023` n `26`; metal avg `-0.0199` n `20`; unknown avg `0.6911` n `951`
- 4h: commodity avg `-0.079` n `12`; crypto_alt avg `0.6274` n `234`; crypto_major avg `0.4457` n `8`; equity avg `0.3211` n `142`; fx avg `0.0695` n `6`; index avg `0.0935` n `26`; metal avg `-0.0044` n `20`; unknown avg `0.2473` n `885`
- 24h: commodity avg `0.1838` n `12`; crypto_alt avg `0.8976` n `234`; crypto_major avg `0.8119` n `8`; equity avg `-0.4078` n `142`; fx avg `0.1459` n `6`; index avg `-0.0339` n `26`; metal avg `-0.3046` n `20`; unknown avg `775.8774` n `797`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
