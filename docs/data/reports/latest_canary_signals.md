# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T18:37:28.734951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0182` n `13`; crypto_alt avg `0.1514` n `239`; crypto_major avg `0.2157` n `8`; equity avg `0.1024` n `168`; fx avg `0.0019` n `6`; index avg `0.0078` n `27`; metal avg `0.0179` n `20`; unknown avg `126.0407` n `1247`
- 1h: commodity avg `0.0372` n `13`; crypto_alt avg `0.3797` n `239`; crypto_major avg `0.437` n `8`; equity avg `0.119` n `168`; fx avg `0.0029` n `6`; index avg `0.0093` n `27`; metal avg `0.0135` n `20`; unknown avg `128.9337` n `1219`
- 4h: commodity avg `0.0751` n `13`; crypto_alt avg `0.1814` n `239`; crypto_major avg `-0.0556` n `8`; equity avg `-0.0714` n `168`; fx avg `-0.0177` n `6`; index avg `-0.0014` n `27`; metal avg `-0.11` n `20`; unknown avg `130.911` n `1195`
- 24h: commodity avg `0.1124` n `13`; crypto_alt avg `2.4402` n `239`; crypto_major avg `1.6729` n `8`; equity avg `2.0931` n `168`; fx avg `-0.0264` n `6`; index avg `0.1506` n `27`; metal avg `0.4823` n `20`; unknown avg `5.026` n `1027`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
