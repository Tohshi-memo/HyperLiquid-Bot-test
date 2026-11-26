# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T22:52:33.293214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0479` n `13`; crypto_alt avg `0.1447` n `239`; crypto_major avg `0.1001` n `8`; equity avg `-0.0082` n `168`; fx avg `0.0026` n `6`; index avg `-0.0064` n `27`; metal avg `-0.0039` n `20`; unknown avg `0.3213` n `1263`
- 1h: commodity avg `0.0429` n `13`; crypto_alt avg `-0.2553` n `239`; crypto_major avg `-0.5241` n `8`; equity avg `-0.2291` n `168`; fx avg `0.0115` n `6`; index avg `-0.0197` n `27`; metal avg `-0.041` n `20`; unknown avg `2.1343` n `1241`
- 4h: commodity avg `0.0337` n `13`; crypto_alt avg `0.0864` n `239`; crypto_major avg `0.1209` n `8`; equity avg `0.1821` n `168`; fx avg `0.0013` n `6`; index avg `0.0108` n `27`; metal avg `0.0221` n `20`; unknown avg `9.0617` n `1177`
- 24h: commodity avg `0.1338` n `13`; crypto_alt avg `1.5846` n `239`; crypto_major avg `0.8172` n `8`; equity avg `0.8915` n `168`; fx avg `-0.0027` n `6`; index avg `0.079` n `27`; metal avg `-0.0155` n `20`; unknown avg `15.1858` n `1013`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
