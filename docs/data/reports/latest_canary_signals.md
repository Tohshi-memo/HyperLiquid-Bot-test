# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T15:37:29.563636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `13`; crypto_alt avg `0.0186` n `235`; crypto_major avg `0.034` n `8`; equity avg `0.015` n `150`; fx avg `-0.0011` n `6`; index avg `0.0016` n `26`; metal avg `-0.0013` n `20`; unknown avg `-0.1664` n `1117`
- 1h: commodity avg `-0.0085` n `13`; crypto_alt avg `0.0101` n `235`; crypto_major avg `-0.1561` n `8`; equity avg `0.0571` n `150`; fx avg `-0.0011` n `6`; index avg `0.0147` n `26`; metal avg `0.0016` n `20`; unknown avg `0.2386` n `1107`
- 4h: commodity avg `0.0859` n `13`; crypto_alt avg `0.8977` n `235`; crypto_major avg `0.6349` n `8`; equity avg `0.1328` n `150`; fx avg `-0.0017` n `6`; index avg `0.0156` n `26`; metal avg `0.0052` n `20`; unknown avg `1.5076` n `1101`
- 24h: commodity avg `-0.5643` n `13`; crypto_alt avg `2.6175` n `235`; crypto_major avg `0.9867` n `8`; equity avg `0.3956` n `150`; fx avg `-0.0031` n `6`; index avg `0.08` n `26`; metal avg `0.0051` n `20`; unknown avg `1.7532` n `958`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
