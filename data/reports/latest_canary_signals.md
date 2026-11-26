# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T20:52:30.371127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0174` n `13`; crypto_alt avg `0.0056` n `239`; crypto_major avg `-0.0723` n `8`; equity avg `-0.0021` n `168`; fx avg `-0.0025` n `6`; index avg `-0.0006` n `27`; metal avg `-0.0008` n `20`; unknown avg `4.4572` n `1237`
- 1h: commodity avg `-0.0275` n `13`; crypto_alt avg `0.0741` n `239`; crypto_major avg `0.1978` n `8`; equity avg `0.0781` n `168`; fx avg `-0.0022` n `6`; index avg `0.0085` n `27`; metal avg `0.0208` n `20`; unknown avg `3.1019` n `1217`
- 4h: commodity avg `0.0554` n `13`; crypto_alt avg `0.7886` n `239`; crypto_major avg `1.0491` n `8`; equity avg `0.353` n `168`; fx avg `-0.0037` n `6`; index avg `0.0341` n `27`; metal avg `-0.0113` n `20`; unknown avg `23.5028` n `1183`
- 24h: commodity avg `0.0859` n `13`; crypto_alt avg `1.9336` n `239`; crypto_major avg `1.1835` n `8`; equity avg `1.538` n `168`; fx avg `-0.03` n `6`; index avg `0.1094` n `27`; metal avg `0.1152` n `20`; unknown avg `13.5582` n `1003`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
