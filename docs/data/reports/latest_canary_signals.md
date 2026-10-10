# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T10:37:22.923950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `13`; crypto_alt avg `0.0224` n `235`; crypto_major avg `-0.0523` n `8`; equity avg `0.0011` n `150`; fx avg `0.0082` n `6`; index avg `-0.0024` n `26`; metal avg `-0.0034` n `20`; unknown avg `0.0251` n `1117`
- 1h: commodity avg `-0.0703` n `13`; crypto_alt avg `-0.273` n `235`; crypto_major avg `-0.2902` n `8`; equity avg `-0.018` n `150`; fx avg `0.0076` n `6`; index avg `0.0013` n `26`; metal avg `0.0022` n `20`; unknown avg `0.5571` n `1115`
- 4h: commodity avg `-0.259` n `13`; crypto_alt avg `-0.4031` n `235`; crypto_major avg `-0.1991` n `8`; equity avg `-0.0667` n `150`; fx avg `-0.0016` n `6`; index avg `-0.0218` n `26`; metal avg `-0.0011` n `20`; unknown avg `1.8468` n `1099`
- 24h: commodity avg `-0.1333` n `13`; crypto_alt avg `1.7862` n `235`; crypto_major avg `0.1611` n `8`; equity avg `-0.1474` n `150`; fx avg `-0.0141` n `6`; index avg `-0.0065` n `26`; metal avg `0.0828` n `20`; unknown avg `631.8971` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
