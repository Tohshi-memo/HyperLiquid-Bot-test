# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T21:22:34.666775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0967` n `13`; crypto_alt avg `-0.1863` n `234`; crypto_major avg `-0.1321` n `8`; equity avg `-0.0499` n `142`; fx avg `0.0215` n `6`; index avg `-0.0032` n `26`; metal avg `0.0115` n `20`; unknown avg `0.1169` n `985`
- 1h: commodity avg `0.1088` n `13`; crypto_alt avg `-0.4135` n `234`; crypto_major avg `-0.3114` n `8`; equity avg `-0.0729` n `142`; fx avg `0.0149` n `6`; index avg `-0.0118` n `26`; metal avg `0.0205` n `20`; unknown avg `2.2318` n `981`
- 4h: commodity avg `0.3115` n `13`; crypto_alt avg `-0.1162` n `234`; crypto_major avg `-0.2795` n `8`; equity avg `0.1989` n `142`; fx avg `0.0528` n `6`; index avg `0.0664` n `26`; metal avg `0.0574` n `20`; unknown avg `1.6584` n `931`
- 24h: commodity avg `0.1666` n `13`; crypto_alt avg `-0.0595` n `234`; crypto_major avg `-0.2472` n `8`; equity avg `1.1184` n `142`; fx avg `-0.1121` n `6`; index avg `0.2263` n `26`; metal avg `-0.0192` n `20`; unknown avg `0.4716` n `856`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
