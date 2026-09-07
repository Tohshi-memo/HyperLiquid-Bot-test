# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T06:22:26.593705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0516` n `12`; crypto_alt avg `0.1001` n `232`; crypto_major avg `-0.0065` n `8`; equity avg `0.0158` n `134`; fx avg `-0.0305` n `6`; index avg `0.016` n `26`; metal avg `0.0493` n `20`; unknown avg `-0.0128` n `794`
- 1h: commodity avg `0.0348` n `12`; crypto_alt avg `-0.1374` n `232`; crypto_major avg `-0.1013` n `8`; equity avg `0.0673` n `134`; fx avg `-0.0703` n `6`; index avg `0.0266` n `26`; metal avg `-0.0029` n `20`; unknown avg `-0.1199` n `774`
- 4h: commodity avg `0.132` n `12`; crypto_alt avg `0.2834` n `232`; crypto_major avg `-0.0885` n `8`; equity avg `0.2465` n `134`; fx avg `-0.059` n `6`; index avg `0.0121` n `26`; metal avg `-0.0555` n `20`; unknown avg `-0.0763` n `740`
- 24h: commodity avg `0.1072` n `12`; crypto_alt avg `0.3983` n `232`; crypto_major avg `-0.5538` n `8`; equity avg `0.4377` n `134`; fx avg `-0.0569` n `6`; index avg `0.0181` n `26`; metal avg `-0.1901` n `20`; unknown avg `378.1448` n `656`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
