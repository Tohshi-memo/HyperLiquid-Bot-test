# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T21:52:33.016907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0363` n `12`; crypto_alt avg `-0.4792` n `228`; crypto_major avg `-0.5371` n `8`; equity avg `-0.0725` n `88`; fx avg `-0.0114` n `6`; index avg `-0.0093` n `23`; metal avg `-0.042` n `20`; unknown avg `-0.1704` n `764`
- 1h: commodity avg `0.0591` n `12`; crypto_alt avg `-0.7053` n `228`; crypto_major avg `-0.5376` n `8`; equity avg `-0.0636` n `88`; fx avg `-0.0241` n `6`; index avg `0.0148` n `23`; metal avg `-0.0398` n `20`; unknown avg `-0.7755` n `764`
- 4h: commodity avg `-0.1617` n `12`; crypto_alt avg `-0.9795` n `228`; crypto_major avg `-0.7998` n `8`; equity avg `0.1031` n `88`; fx avg `-0.0724` n `6`; index avg `0.0673` n `23`; metal avg `0.0157` n `20`; unknown avg `0.5094` n `764`
- 24h: commodity avg `0.0121` n `12`; crypto_alt avg `-0.7907` n `228`; crypto_major avg `-1.1837` n `8`; equity avg `0.1942` n `88`; fx avg `-0.0979` n `6`; index avg `0.0283` n `23`; metal avg `0.005` n `20`; unknown avg `15.0687` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1956`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
