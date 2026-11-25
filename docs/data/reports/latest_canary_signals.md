# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T00:22:27.761924+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `13`; crypto_alt avg `-0.0296` n `239`; crypto_major avg `0.052` n `8`; equity avg `-0.0787` n `168`; fx avg `0.016` n `6`; index avg `0.0063` n `27`; metal avg `-0.0345` n `20`; unknown avg `160.0376` n `1257`
- 1h: commodity avg `-0.0002` n `13`; crypto_alt avg `-0.2845` n `239`; crypto_major avg `-0.4655` n `8`; equity avg `-0.6601` n `168`; fx avg `0.0751` n `6`; index avg `-0.0576` n `27`; metal avg `-0.153` n `20`; unknown avg `173.1022` n `1247`
- 4h: commodity avg `0.0551` n `13`; crypto_alt avg `0.0294` n `239`; crypto_major avg `0.1516` n `8`; equity avg `-0.2723` n `168`; fx avg `0.0529` n `6`; index avg `-0.0167` n `27`; metal avg `-0.0602` n `20`; unknown avg `23.5387` n `1159`
- 24h: commodity avg `0.5679` n `13`; crypto_alt avg `-3.3166` n `239`; crypto_major avg `-2.603` n `8`; equity avg `-4.6919` n `167`; fx avg `0.2954` n `6`; index avg `-0.4381` n `27`; metal avg `-1.2744` n `20`; unknown avg `477.9272` n `1049`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
