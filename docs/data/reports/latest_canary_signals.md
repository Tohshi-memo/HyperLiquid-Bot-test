# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T06:22:24.847356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `13`; crypto_alt avg `0.1287` n `235`; crypto_major avg `0.05` n `8`; equity avg `0.0103` n `150`; fx avg `0.0` n `6`; index avg `0.0004` n `26`; metal avg `0.002` n `20`; unknown avg `1.1049` n `1117`
- 1h: commodity avg `0.0` n `5`; crypto_alt avg `0.0854` n `235`; crypto_major avg `-0.1072` n `8`; equity avg `-0.0038` n `41`; fx avg `0.0` n `1`; index avg `0.0` n `17`; metal avg `0.0005` n `12`; unknown avg `0.4597` n `1069`
- 4h: commodity avg `0.0965` n `13`; crypto_alt avg `-0.6252` n `235`; crypto_major avg `-0.4262` n `8`; equity avg `-0.1026` n `150`; fx avg `-0.0019` n `6`; index avg `-0.0167` n `26`; metal avg `-0.0096` n `20`; unknown avg `0.6178` n `1093`
- 24h: commodity avg `0.1349` n `13`; crypto_alt avg `0.623` n `235`; crypto_major avg `-0.1651` n `8`; equity avg `-0.0164` n `150`; fx avg `-0.0107` n `6`; index avg `-0.0371` n `26`; metal avg `0.0015` n `20`; unknown avg `0.3559` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
