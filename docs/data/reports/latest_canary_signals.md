# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T19:37:27.701427+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0157` n `13`; crypto_alt avg `-0.0639` n `239`; crypto_major avg `0.0269` n `8`; equity avg `0.0573` n `168`; fx avg `0.0002` n `6`; index avg `-0.0005` n `27`; metal avg `0.0171` n `20`; unknown avg `9.129` n `1263`
- 1h: commodity avg `0.0133` n `13`; crypto_alt avg `0.2431` n `239`; crypto_major avg `0.414` n `8`; equity avg `0.246` n `168`; fx avg `-0.0075` n `6`; index avg `0.0171` n `27`; metal avg `-0.0117` n `20`; unknown avg `26.4981` n `1259`
- 4h: commodity avg `-0.0159` n `13`; crypto_alt avg `1.1317` n `239`; crypto_major avg `1.1386` n `8`; equity avg `0.3049` n `168`; fx avg `-0.0119` n `6`; index avg `0.0231` n `27`; metal avg `-0.0917` n `20`; unknown avg `358.4475` n `1197`
- 24h: commodity avg `0.1927` n `13`; crypto_alt avg `1.525` n `239`; crypto_major avg `0.8427` n `8`; equity avg `1.0841` n `168`; fx avg `-0.0406` n `6`; index avg `0.07` n `27`; metal avg `0.2413` n `20`; unknown avg `31.4195` n `1027`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
