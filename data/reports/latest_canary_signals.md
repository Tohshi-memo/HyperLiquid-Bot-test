# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T13:46:36.459941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0885` n `12`; crypto_alt avg `0.0958` n `229`; crypto_major avg `0.1348` n `8`; equity avg `-0.2666` n `91`; fx avg `-0.0114` n `6`; index avg `-0.0052` n `25`; metal avg `0.049` n `20`; unknown avg `0.0151` n `766`
- 1h: commodity avg `-0.2043` n `12`; crypto_alt avg `0.1654` n `229`; crypto_major avg `0.3083` n `8`; equity avg `-0.5085` n `91`; fx avg `-0.0354` n `6`; index avg `-0.0119` n `25`; metal avg `0.0413` n `20`; unknown avg `-0.1018` n `766`
- 4h: commodity avg `-0.2058` n `12`; crypto_alt avg `0.1569` n `229`; crypto_major avg `-0.0379` n `8`; equity avg `-0.2512` n `91`; fx avg `-0.0336` n `6`; index avg `0.0008` n `25`; metal avg `0.0539` n `20`; unknown avg `-0.0813` n `766`
- 24h: commodity avg `-0.7866` n `12`; crypto_alt avg `1.09` n `229`; crypto_major avg `1.5071` n `8`; equity avg `-0.9595` n `91`; fx avg `-0.1341` n `6`; index avg `-0.0607` n `25`; metal avg `-0.1909` n `20`; unknown avg `-0.1366` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
