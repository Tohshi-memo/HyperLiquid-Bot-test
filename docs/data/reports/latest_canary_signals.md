# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T19:37:24.820794+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0208` n `12`; crypto_alt avg `0.0663` n `231`; crypto_major avg `0.1022` n `8`; equity avg `0.0327` n `122`; fx avg `0.0004` n `6`; index avg `-0.0037` n `25`; metal avg `0.0233` n `20`; unknown avg `0.0794` n `797`
- 1h: commodity avg `-0.0156` n `12`; crypto_alt avg `0.0401` n `231`; crypto_major avg `0.065` n `8`; equity avg `0.157` n `122`; fx avg `-0.0051` n `6`; index avg `0.0373` n `25`; metal avg `0.008` n `20`; unknown avg `0.0088` n `797`
- 4h: commodity avg `-0.0028` n `12`; crypto_alt avg `0.347` n `231`; crypto_major avg `0.524` n `8`; equity avg `0.3698` n `122`; fx avg `-0.0031` n `6`; index avg `0.0354` n `25`; metal avg `-0.107` n `20`; unknown avg `0.2218` n `797`
- 24h: commodity avg `0.1086` n `12`; crypto_alt avg `-1.0927` n `231`; crypto_major avg `-1.1325` n `8`; equity avg `0.0725` n `122`; fx avg `-0.0508` n `6`; index avg `0.061` n `25`; metal avg `-0.3927` n `20`; unknown avg `0.5836` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
