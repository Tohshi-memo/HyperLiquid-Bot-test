# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T01:22:36.648344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0652` n `13`; crypto_alt avg `-0.0508` n `239`; crypto_major avg `-0.0726` n `8`; equity avg `-0.0072` n `160`; fx avg `-0.0003` n `6`; index avg `0.0056` n `27`; metal avg `-0.0022` n `20`; unknown avg `-0.0768` n `1259`
- 1h: commodity avg `-0.047` n `13`; crypto_alt avg `0.0884` n `239`; crypto_major avg `0.1067` n `8`; equity avg `-0.5739` n `160`; fx avg `-0.0058` n `6`; index avg `-0.0696` n `27`; metal avg `0.097` n `20`; unknown avg `0.716` n `1253`
- 4h: commodity avg `-0.1527` n `13`; crypto_alt avg `-0.3479` n `239`; crypto_major avg `0.1369` n `8`; equity avg `-0.1427` n `160`; fx avg `0.0584` n `6`; index avg `-0.0863` n `27`; metal avg `0.0407` n `20`; unknown avg `19.2923` n `1241`
- 24h: commodity avg `-0.3682` n `13`; crypto_alt avg `1.0048` n `239`; crypto_major avg `0.0347` n `8`; equity avg `4.7873` n `160`; fx avg `-0.0301` n `6`; index avg `0.4592` n `27`; metal avg `0.264` n `20`; unknown avg `5.1058` n `1066`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
