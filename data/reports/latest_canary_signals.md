# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T04:37:39.791033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0195` n `12`; crypto_alt avg `-0.0684` n `234`; crypto_major avg `-0.0636` n `8`; equity avg `0.0964` n `142`; fx avg `0.0081` n `6`; index avg `0.0232` n `26`; metal avg `0.0225` n `20`; unknown avg `1.5815` n `963`
- 1h: commodity avg `-0.0001` n `12`; crypto_alt avg `0.4` n `234`; crypto_major avg `0.0429` n `8`; equity avg `0.1156` n `142`; fx avg `0.0373` n `6`; index avg `0.0332` n `26`; metal avg `-0.0005` n `20`; unknown avg `6.656` n `955`
- 4h: commodity avg `0.0497` n `12`; crypto_alt avg `0.6571` n `234`; crypto_major avg `0.1773` n `8`; equity avg `-0.117` n `142`; fx avg `-0.0589` n `6`; index avg `-0.0032` n `26`; metal avg `-0.0765` n `20`; unknown avg `4.6695` n `955`
- 24h: commodity avg `-1.0016` n `12`; crypto_alt avg `1.7792` n `234`; crypto_major avg `0.3473` n `8`; equity avg `1.2383` n `142`; fx avg `-0.1298` n `6`; index avg `0.2215` n `26`; metal avg `0.2874` n `20`; unknown avg `3235.5756` n `834`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
