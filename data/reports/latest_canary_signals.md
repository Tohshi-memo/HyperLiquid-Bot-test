# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T17:22:30.430765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1116` n `13`; crypto_alt avg `0.6658` n `239`; crypto_major avg `0.2937` n `8`; equity avg `0.4816` n `168`; fx avg `0.014` n `6`; index avg `0.0623` n `27`; metal avg `0.1565` n `20`; unknown avg `0.8983` n `1264`
- 1h: commodity avg `0.1813` n `13`; crypto_alt avg `1.7075` n `239`; crypto_major avg `0.9445` n `8`; equity avg `2.0786` n `168`; fx avg `0.0627` n `6`; index avg `0.224` n `27`; metal avg `0.4884` n `20`; unknown avg `26.1655` n `1262`
- 4h: commodity avg `0.3759` n `13`; crypto_alt avg `1.5193` n `239`; crypto_major avg `1.111` n `8`; equity avg `-0.0004` n `168`; fx avg `0.0845` n `6`; index avg `0.029` n `27`; metal avg `-0.0517` n `20`; unknown avg `358.8054` n `1243`
- 24h: commodity avg `0.4913` n `13`; crypto_alt avg `0.269` n `239`; crypto_major avg `-0.7097` n `8`; equity avg `-3.2914` n `168`; fx avg `-0.0018` n `6`; index avg `-0.3477` n `27`; metal avg `-0.5121` n `20`; unknown avg `638.769` n `1065`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
