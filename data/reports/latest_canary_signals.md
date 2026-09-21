# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T05:22:27.557050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0127` n `12`; crypto_alt avg `0.1017` n `234`; crypto_major avg `0.19` n `8`; equity avg `-0.0047` n `140`; fx avg `-0.0008` n `6`; index avg `-0.0021` n `26`; metal avg `0.016` n `20`; unknown avg `680.9745` n `944`
- 1h: commodity avg `0.0667` n `12`; crypto_alt avg `0.077` n `234`; crypto_major avg `0.2252` n `8`; equity avg `-0.1385` n `140`; fx avg `0.0128` n `6`; index avg `-0.0234` n `26`; metal avg `-0.0474` n `20`; unknown avg `18.9869` n `942`
- 4h: commodity avg `0.1234` n `12`; crypto_alt avg `-0.1633` n `234`; crypto_major avg `-0.8841` n `8`; equity avg `-0.2795` n `140`; fx avg `0.0134` n `6`; index avg `0.0098` n `26`; metal avg `-0.0906` n `20`; unknown avg `72.1481` n `936`
- 24h: commodity avg `-0.5583` n `12`; crypto_alt avg `3.5573` n `234`; crypto_major avg `2.6034` n `8`; equity avg `1.0057` n `140`; fx avg `0.001` n `6`; index avg `0.2049` n `26`; metal avg `0.0198` n `20`; unknown avg `8.6638` n `763`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
