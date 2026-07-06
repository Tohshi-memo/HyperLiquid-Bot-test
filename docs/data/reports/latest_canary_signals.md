# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T13:52:31.967557+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1212` n `12`; crypto_alt avg `0.7103` n `229`; crypto_major avg `0.7582` n `8`; equity avg `0.9073` n `88`; fx avg `-0.0088` n `6`; index avg `0.1` n `25`; metal avg `0.0522` n `20`; unknown avg `0.393` n `765`
- 1h: commodity avg `0.1439` n `12`; crypto_alt avg `0.5299` n `229`; crypto_major avg `0.2496` n `8`; equity avg `0.501` n `88`; fx avg `0.0073` n `6`; index avg `0.0634` n `25`; metal avg `0.213` n `20`; unknown avg `-0.1449` n `765`
- 4h: commodity avg `0.0656` n `12`; crypto_alt avg `-0.1955` n `229`; crypto_major avg `-0.6606` n `8`; equity avg `0.3506` n `88`; fx avg `0.0262` n `6`; index avg `0.077` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.2685` n `765`
- 24h: commodity avg `-0.0619` n `12`; crypto_alt avg `-0.7776` n `229`; crypto_major avg `-0.8642` n `8`; equity avg `-0.3805` n `88`; fx avg `0.1396` n `6`; index avg `0.0315` n `25`; metal avg `-0.3057` n `20`; unknown avg `0.5434` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
