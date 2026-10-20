# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T08:37:32.166376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0731` n `13`; crypto_alt avg `-0.0413` n `237`; crypto_major avg `0.0495` n `8`; equity avg `0.2289` n `151`; fx avg `0.0047` n `6`; index avg `0.0415` n `26`; metal avg `0.058` n `20`; unknown avg `0.8228` n `1198`
- 1h: commodity avg `0.0425` n `13`; crypto_alt avg `-0.1122` n `237`; crypto_major avg `-0.0035` n `8`; equity avg `0.1514` n `151`; fx avg `0.0087` n `6`; index avg `0.0443` n `26`; metal avg `0.0219` n `20`; unknown avg `0.09` n `1180`
- 4h: commodity avg `0.1912` n `13`; crypto_alt avg `-0.8161` n `237`; crypto_major avg `-0.732` n `8`; equity avg `-0.1752` n `151`; fx avg `0.0021` n `6`; index avg `0.0248` n `26`; metal avg `-0.0343` n `20`; unknown avg `3.3769` n `1160`
- 24h: commodity avg `0.4745` n `13`; crypto_alt avg `-0.5089` n `237`; crypto_major avg `-1.1257` n `8`; equity avg `-1.3619` n `151`; fx avg `0.0167` n `6`; index avg `-0.193` n `26`; metal avg `-0.1455` n `20`; unknown avg `4.6651` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
