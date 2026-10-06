# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T10:07:31.975415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `13`; crypto_alt avg `-0.0062` n `235`; crypto_major avg `-0.0225` n `8`; equity avg `0.0056` n `150`; fx avg `0.0077` n `6`; index avg `-0.0077` n `26`; metal avg `-0.0214` n `20`; unknown avg `0.2676` n `1072`
- 1h: commodity avg `-0.1262` n `13`; crypto_alt avg `-0.0578` n `235`; crypto_major avg `-0.1588` n `8`; equity avg `0.0106` n `149`; fx avg `0.0152` n `6`; index avg `-0.0153` n `26`; metal avg `-0.0421` n `20`; unknown avg `0.1167` n `1072`
- 4h: commodity avg `-0.4635` n `13`; crypto_alt avg `0.8301` n `235`; crypto_major avg `0.542` n `8`; equity avg `0.1912` n `149`; fx avg `0.0718` n `6`; index avg `0.0303` n `26`; metal avg `0.1671` n `20`; unknown avg `1.2064` n `992`
- 24h: commodity avg `-0.6782` n `13`; crypto_alt avg `-0.8468` n `235`; crypto_major avg `-0.519` n `8`; equity avg `0.5023` n `149`; fx avg `0.0418` n `6`; index avg `0.2149` n `26`; metal avg `-0.1353` n `20`; unknown avg `-0.0438` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
