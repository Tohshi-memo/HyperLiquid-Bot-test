# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T21:52:24.917711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `-0.1271` n `232`; crypto_major avg `-0.0626` n `8`; equity avg `-0.0204` n `134`; fx avg `0.0018` n `6`; index avg `-0.0003` n `26`; metal avg `0.0065` n `20`; unknown avg `-0.091` n `796`
- 1h: commodity avg `0.0033` n `12`; crypto_alt avg `-0.1277` n `232`; crypto_major avg `-0.2104` n `8`; equity avg `0.03` n `134`; fx avg `-0.0022` n `6`; index avg `0.0076` n `26`; metal avg `0.0056` n `20`; unknown avg `-0.0872` n `786`
- 4h: commodity avg `-0.0289` n `12`; crypto_alt avg `0.1515` n `232`; crypto_major avg `-0.1394` n `8`; equity avg `0.0882` n `134`; fx avg `-0.0064` n `6`; index avg `0.0214` n `26`; metal avg `0.0298` n `20`; unknown avg `73.8891` n `734`
- 24h: commodity avg `0.1711` n `12`; crypto_alt avg `-0.2223` n `232`; crypto_major avg `-1.3323` n `8`; equity avg `0.4692` n `134`; fx avg `-0.1482` n `6`; index avg `0.0861` n `26`; metal avg `0.0457` n `20`; unknown avg `7800.5678` n `641`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
