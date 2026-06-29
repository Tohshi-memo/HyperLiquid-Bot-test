# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T01:37:30.333349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0176` n `12`; crypto_alt avg `0.186` n `228`; crypto_major avg `0.1352` n `8`; equity avg `0.1096` n `88`; fx avg `0.0208` n `6`; index avg `0.0302` n `23`; metal avg `0.0205` n `20`; unknown avg `0.6354` n `764`
- 1h: commodity avg `0.0873` n `12`; crypto_alt avg `0.7358` n `228`; crypto_major avg `0.7495` n `8`; equity avg `0.4055` n `88`; fx avg `0.0148` n `6`; index avg `0.1223` n `23`; metal avg `0.057` n `20`; unknown avg `0.4091` n `764`
- 4h: commodity avg `-0.1095` n `12`; crypto_alt avg `0.1269` n `228`; crypto_major avg `-0.1543` n `8`; equity avg `-0.4619` n `88`; fx avg `0.0563` n `6`; index avg `-0.1596` n `23`; metal avg `-0.2667` n `20`; unknown avg `1.4529` n `762`
- 24h: commodity avg `-0.4405` n `12`; crypto_alt avg `-0.3485` n `228`; crypto_major avg `-0.7085` n `8`; equity avg `-0.0873` n `88`; fx avg `-0.0087` n `6`; index avg `-0.0323` n `23`; metal avg `-0.2501` n `20`; unknown avg `15.5843` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1888`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
