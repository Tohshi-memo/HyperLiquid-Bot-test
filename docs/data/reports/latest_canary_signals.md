# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T09:37:26.600101+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0652` n `13`; crypto_alt avg `0.1816` n `239`; crypto_major avg `0.3771` n `8`; equity avg `-0.1399` n `168`; fx avg `0.0096` n `6`; index avg `-0.0367` n `27`; metal avg `0.034` n `20`; unknown avg `0.0365` n `1263`
- 1h: commodity avg `-0.0433` n `13`; crypto_alt avg `0.26` n `239`; crypto_major avg `0.4156` n `8`; equity avg `0.3641` n `168`; fx avg `-0.0111` n `6`; index avg `-0.0056` n `27`; metal avg `0.1291` n `20`; unknown avg `224.1614` n `1175`
- 4h: commodity avg `-0.2217` n `13`; crypto_alt avg `0.2806` n `239`; crypto_major avg `0.3968` n `8`; equity avg `0.3245` n `168`; fx avg `-0.0771` n `6`; index avg `-0.0434` n `27`; metal avg `0.2797` n `20`; unknown avg `238.914` n `1105`
- 24h: commodity avg `0.3786` n `13`; crypto_alt avg `2.0947` n `239`; crypto_major avg `2.8385` n `8`; equity avg `4.259` n `168`; fx avg `-0.104` n `6`; index avg `0.3166` n `27`; metal avg `1.2543` n `20`; unknown avg `52.1403` n `1029`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
