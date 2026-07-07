# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T12:52:32.586248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0718` n `12`; crypto_alt avg `-0.0727` n `229`; crypto_major avg `0.0097` n `8`; equity avg `-0.1678` n `91`; fx avg `0.0247` n `6`; index avg `-0.0327` n `25`; metal avg `-0.019` n `20`; unknown avg `-0.1209` n `763`
- 1h: commodity avg `-0.111` n `12`; crypto_alt avg `0.0258` n `229`; crypto_major avg `0.2184` n `8`; equity avg `0.0586` n `91`; fx avg `-0.0104` n `6`; index avg `0.0811` n `25`; metal avg `0.0952` n `20`; unknown avg `-0.0429` n `763`
- 4h: commodity avg `-0.3089` n `12`; crypto_alt avg `0.5168` n `229`; crypto_major avg `0.5568` n `8`; equity avg `-0.267` n `91`; fx avg `-0.0826` n `6`; index avg `-0.0077` n `25`; metal avg `0.3639` n `20`; unknown avg `0.15` n `757`
- 24h: commodity avg `0.2112` n `12`; crypto_alt avg `1.793` n `229`; crypto_major avg `1.5343` n `8`; equity avg `-1.4312` n `90`; fx avg `-0.1606` n `6`; index avg `-0.3715` n `25`; metal avg `0.3117` n `20`; unknown avg `-0.2716` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
