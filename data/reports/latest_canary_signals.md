# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T15:52:26.891002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `0.0403` n `232`; crypto_major avg `0.0967` n `8`; equity avg `0.027` n `128`; fx avg `-0.0129` n `6`; index avg `0.0103` n `26`; metal avg `-0.0124` n `20`; unknown avg `0.0101` n `794`
- 1h: commodity avg `0.0439` n `12`; crypto_alt avg `-0.1686` n `232`; crypto_major avg `0.1663` n `8`; equity avg `0.1258` n `128`; fx avg `0.0052` n `6`; index avg `-0.0306` n `26`; metal avg `-0.047` n `20`; unknown avg `0.0112` n `792`
- 4h: commodity avg `-0.1621` n `12`; crypto_alt avg `-0.1031` n `232`; crypto_major avg `0.3926` n `8`; equity avg `0.0789` n `128`; fx avg `0.0685` n `6`; index avg `-0.0892` n `26`; metal avg `-0.3384` n `20`; unknown avg `0.1351` n `790`
- 24h: commodity avg `0.5681` n `12`; crypto_alt avg `-0.8848` n `231`; crypto_major avg `-1.2478` n `8`; equity avg `-0.4566` n `128`; fx avg `-0.0797` n `6`; index avg `-0.207` n `26`; metal avg `-0.5511` n `20`; unknown avg `0.2611` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
