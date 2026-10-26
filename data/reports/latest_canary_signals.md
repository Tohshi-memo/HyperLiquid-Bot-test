# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T09:37:31.271495+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0779` n `13`; crypto_alt avg `0.1884` n `237`; crypto_major avg `0.1543` n `8`; equity avg `0.1198` n `152`; fx avg `-0.0012` n `6`; index avg `0.0026` n `26`; metal avg `0.0513` n `20`; unknown avg `0.391` n `1240`
- 1h: commodity avg `0.0418` n `13`; crypto_alt avg `0.3407` n `237`; crypto_major avg `0.2324` n `8`; equity avg `0.4115` n `152`; fx avg `0.0014` n `6`; index avg `0.0609` n `26`; metal avg `0.0504` n `20`; unknown avg `0.2054` n `1240`
- 4h: commodity avg `0.1252` n `13`; crypto_alt avg `0.311` n `237`; crypto_major avg `0.2816` n `8`; equity avg `0.0024` n `152`; fx avg `0.0118` n `6`; index avg `0.0182` n `26`; metal avg `0.0256` n `20`; unknown avg `-0.0661` n `1126`
- 24h: commodity avg `-0.4343` n `13`; crypto_alt avg `0.9561` n `237`; crypto_major avg `0.6969` n `8`; equity avg `0.0927` n `152`; fx avg `0.0674` n `6`; index avg `0.054` n `26`; metal avg `0.2535` n `20`; unknown avg `-0.2807` n `955`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2586`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2073`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
