# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T08:22:35.149330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0931` n `13`; crypto_alt avg `0.2572` n `237`; crypto_major avg `0.2501` n `8`; equity avg `-0.0449` n `152`; fx avg `0.0143` n `6`; index avg `0.0103` n `26`; metal avg `0.0184` n `20`; unknown avg `0.0893` n `1208`
- 1h: commodity avg `0.1048` n `13`; crypto_alt avg `-0.2919` n `237`; crypto_major avg `-0.2303` n `8`; equity avg `-0.3774` n `152`; fx avg `0.0138` n `6`; index avg `-0.0177` n `26`; metal avg `0.0893` n `20`; unknown avg `4.5179` n `1144`
- 4h: commodity avg `0.22` n `13`; crypto_alt avg `0.019` n `237`; crypto_major avg `0.1129` n `8`; equity avg `-0.4401` n `152`; fx avg `0.018` n `6`; index avg `-0.0784` n `26`; metal avg `0.0122` n `20`; unknown avg `4.2358` n `1124`
- 24h: commodity avg `-0.4272` n `13`; crypto_alt avg `-0.684` n `237`; crypto_major avg `-0.6236` n `8`; equity avg `-0.8433` n `152`; fx avg `0.0602` n `6`; index avg `-0.0508` n `26`; metal avg `0.1819` n `20`; unknown avg `-0.4312` n `953`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2517`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2023`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
