# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T06:22:24.371660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0461` n `12`; crypto_alt avg `0.1815` n `232`; crypto_major avg `0.1436` n `8`; equity avg `-0.0729` n `133`; fx avg `0.0159` n `6`; index avg `-0.0234` n `26`; metal avg `-0.0569` n `20`; unknown avg `-0.0271` n `792`
- 1h: commodity avg `-0.1231` n `12`; crypto_alt avg `0.6091` n `232`; crypto_major avg `0.6639` n `8`; equity avg `0.423` n `133`; fx avg `-0.0513` n `6`; index avg `0.1141` n `26`; metal avg `0.062` n `20`; unknown avg `14.9903` n `756`
- 4h: commodity avg `-0.2868` n `12`; crypto_alt avg `0.7271` n `232`; crypto_major avg `0.3923` n `8`; equity avg `-0.1867` n `133`; fx avg `-0.057` n `6`; index avg `-0.0534` n `26`; metal avg `0.0491` n `20`; unknown avg `0.1431` n `756`
- 24h: commodity avg `-0.0667` n `12`; crypto_alt avg `0.7661` n `232`; crypto_major avg `0.527` n `8`; equity avg `1.2088` n `133`; fx avg `-0.3432` n `6`; index avg `0.1475` n `26`; metal avg `0.7123` n `20`; unknown avg `-0.4513` n `735`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0422`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0399`, n `668`, weak_sample_signal
