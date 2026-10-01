# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T20:52:30.060240+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `13`; crypto_alt avg `-0.0502` n `234`; crypto_major avg `-0.015` n `8`; equity avg `-0.0023` n `142`; fx avg `-0.0003` n `6`; index avg `-0.0031` n `26`; metal avg `0.0247` n `20`; unknown avg `-0.3805` n `985`
- 1h: commodity avg `-0.069` n `13`; crypto_alt avg `-0.0378` n `234`; crypto_major avg `-0.0614` n `8`; equity avg `-0.0741` n `142`; fx avg `-0.0044` n `6`; index avg `-0.0292` n `26`; metal avg `-0.0178` n `20`; unknown avg `2.8509` n `933`
- 4h: commodity avg `0.186` n `13`; crypto_alt avg `1.0006` n `234`; crypto_major avg `0.6082` n `8`; equity avg `0.7227` n `142`; fx avg `0.0164` n `6`; index avg `0.1655` n `26`; metal avg `0.1641` n `20`; unknown avg `0.7451` n `933`
- 24h: commodity avg `0.0162` n `13`; crypto_alt avg `0.1154` n `234`; crypto_major avg `-0.0408` n `8`; equity avg `1.0478` n `142`; fx avg `-0.1059` n `6`; index avg `0.2128` n `26`; metal avg `-0.0327` n `20`; unknown avg `0.4222` n `856`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1701`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
