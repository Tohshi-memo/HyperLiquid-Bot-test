# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T04:07:28.303339+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0113` n `13`; crypto_alt avg `0.0586` n `239`; crypto_major avg `-0.1053` n `8`; equity avg `-0.0813` n `168`; fx avg `0.0034` n `6`; index avg `0.0063` n `27`; metal avg `-0.0449` n `20`; unknown avg `-0.1422` n `1247`
- 1h: commodity avg `-0.0361` n `13`; crypto_alt avg `0.1991` n `239`; crypto_major avg `0.0192` n `8`; equity avg `0.1639` n `168`; fx avg `-0.0095` n `6`; index avg `0.0253` n `27`; metal avg `-0.0881` n `20`; unknown avg `25.7916` n `1247`
- 4h: commodity avg `-0.2654` n `13`; crypto_alt avg `-0.1668` n `239`; crypto_major avg `-0.7317` n `8`; equity avg `-0.9249` n `168`; fx avg `-0.07` n `6`; index avg `-0.0669` n `27`; metal avg `-0.1257` n `20`; unknown avg `165.5523` n `1225`
- 24h: commodity avg `0.4723` n `13`; crypto_alt avg `-2.8543` n `239`; crypto_major avg `-2.7306` n `8`; equity avg `-5.0807` n `167`; fx avg `0.1558` n `6`; index avg `-0.509` n `27`; metal avg `-0.9533` n `20`; unknown avg `495.4345` n `1031`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
