# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T22:22:26.146695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `13`; crypto_alt avg `-0.0093` n `239`; crypto_major avg `-0.0913` n `8`; equity avg `-0.0598` n `168`; fx avg `0.0111` n `6`; index avg `-0.0061` n `27`; metal avg `-0.0094` n `20`; unknown avg `7.2305` n `1261`
- 1h: commodity avg `-0.0128` n `13`; crypto_alt avg `-0.1792` n `239`; crypto_major avg `-0.4739` n `8`; equity avg `-0.0796` n `168`; fx avg `0.0101` n `6`; index avg `-0.002` n `27`; metal avg `-0.0181` n `20`; unknown avg `2.4075` n `1243`
- 4h: commodity avg `-0.0093` n `13`; crypto_alt avg `0.3206` n `239`; crypto_major avg `0.399` n `8`; equity avg `0.4383` n `168`; fx avg `0.0053` n `6`; index avg `0.0371` n `27`; metal avg `0.0446` n `20`; unknown avg `27.562` n `1165`
- 24h: commodity avg `0.0543` n `13`; crypto_alt avg `1.6357` n `239`; crypto_major avg `0.8886` n `8`; equity avg `1.3594` n `168`; fx avg `-0.0027` n `6`; index avg `0.1099` n `27`; metal avg `0.0078` n `20`; unknown avg `14.8046` n `1015`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
