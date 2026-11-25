# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T03:22:35.923126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0117` n `13`; crypto_alt avg `0.4959` n `239`; crypto_major avg `0.5118` n `8`; equity avg `0.2871` n `168`; fx avg `0.0237` n `6`; index avg `0.0286` n `27`; metal avg `0.0575` n `20`; unknown avg `24.1813` n `1261`
- 1h: commodity avg `-0.0605` n `13`; crypto_alt avg `0.682` n `239`; crypto_major avg `0.7798` n `8`; equity avg `0.0785` n `168`; fx avg `-0.0079` n `6`; index avg `0.0553` n `27`; metal avg `-0.157` n `20`; unknown avg `0.8594` n `1259`
- 4h: commodity avg `-0.2413` n `13`; crypto_alt avg `-0.1335` n `239`; crypto_major avg `-0.7592` n `8`; equity avg `-1.3744` n `168`; fx avg `0.0221` n `6`; index avg `-0.1266` n `27`; metal avg `-0.0991` n `20`; unknown avg `175.866` n `1227`
- 24h: commodity avg `0.4402` n `13`; crypto_alt avg `-2.0227` n `239`; crypto_major avg `-1.4902` n `8`; equity avg `-4.5817` n `167`; fx avg `0.189` n `6`; index avg `-0.4662` n `27`; metal avg `-0.8817` n `20`; unknown avg `493.554` n `1025`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
