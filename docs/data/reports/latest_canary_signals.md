# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T23:52:35.276367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `13`; crypto_alt avg `-0.043` n `239`; crypto_major avg `-0.0317` n `8`; equity avg `-0.1024` n `168`; fx avg `0.0167` n `6`; index avg `-0.013` n `27`; metal avg `-0.0581` n `20`; unknown avg `0.9121` n `1265`
- 1h: commodity avg `0.0177` n `13`; crypto_alt avg `-0.3364` n `239`; crypto_major avg `-0.3699` n `8`; equity avg `-0.5783` n `168`; fx avg `0.0161` n `6`; index avg `-0.0357` n `27`; metal avg `-0.0529` n `20`; unknown avg `83.7053` n `1235`
- 4h: commodity avg `0.0049` n `13`; crypto_alt avg `-0.2071` n `239`; crypto_major avg `0.1425` n `8`; equity avg `-0.1977` n `168`; fx avg `0.0047` n `6`; index avg `-0.0281` n `27`; metal avg `-0.0375` n `20`; unknown avg `23.613` n `1165`
- 24h: commodity avg `0.5883` n `13`; crypto_alt avg `-2.7884` n `239`; crypto_major avg `-2.1983` n `8`; equity avg `-4.0665` n `167`; fx avg `0.243` n `6`; index avg `-0.1947` n `27`; metal avg `-1.022` n `20`; unknown avg `465.584` n `1055`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
