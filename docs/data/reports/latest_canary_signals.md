# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T14:07:27.131556+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.034` n `12`; crypto_alt avg `-0.2726` n `229`; crypto_major avg `-0.505` n `8`; equity avg `-0.293` n `91`; fx avg `-0.0202` n `6`; index avg `-0.0141` n `25`; metal avg `-0.013` n `20`; unknown avg `0.0343` n `766`
- 1h: commodity avg `-0.244` n `12`; crypto_alt avg `0.0501` n `229`; crypto_major avg `0.0013` n `8`; equity avg `-0.41` n `91`; fx avg `-0.0607` n `6`; index avg `0.0577` n `25`; metal avg `0.0529` n `20`; unknown avg `0.0001` n `766`
- 4h: commodity avg `-0.3567` n `12`; crypto_alt avg `-0.019` n `229`; crypto_major avg `-0.3168` n `8`; equity avg `-0.3922` n `91`; fx avg `-0.0608` n `6`; index avg `0.0302` n `25`; metal avg `0.0838` n `20`; unknown avg `-0.1161` n `766`
- 24h: commodity avg `-0.8831` n `12`; crypto_alt avg `0.8663` n `229`; crypto_major avg `1.3244` n `8`; equity avg `-0.9829` n `91`; fx avg `-0.1758` n `6`; index avg `-0.0107` n `25`; metal avg `-0.1651` n `20`; unknown avg `-0.2161` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
