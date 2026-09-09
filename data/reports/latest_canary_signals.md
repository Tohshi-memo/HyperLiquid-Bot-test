# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T05:52:25.217794+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.1731` n `233`; crypto_major avg `-0.1863` n `8`; equity avg `0.0208` n `134`; fx avg `0.029` n `6`; index avg `0.0174` n `26`; metal avg `0.0556` n `20`; unknown avg `0.2635` n `798`
- 1h: commodity avg `-0.048` n `12`; crypto_alt avg `-0.3305` n `233`; crypto_major avg `-0.4888` n `8`; equity avg `-0.1269` n `134`; fx avg `-0.0028` n `6`; index avg `-0.0145` n `26`; metal avg `0.14` n `20`; unknown avg `0.7145` n `796`
- 4h: commodity avg `-0.1307` n `12`; crypto_alt avg `0.3065` n `233`; crypto_major avg `0.0765` n `8`; equity avg `-0.0977` n `134`; fx avg `-0.0253` n `6`; index avg `-0.0058` n `26`; metal avg `0.1764` n `20`; unknown avg `0.1401` n `785`
- 24h: commodity avg `-0.2191` n `12`; crypto_alt avg `-0.2457` n `232`; crypto_major avg `0.8203` n `8`; equity avg `0.6582` n `134`; fx avg `-0.0533` n `6`; index avg `-0.054` n `26`; metal avg `-0.1583` n `20`; unknown avg `1.3101` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
