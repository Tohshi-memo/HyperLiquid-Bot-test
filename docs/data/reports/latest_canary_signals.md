# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T10:07:31.708621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0403` n `12`; crypto_alt avg `-0.0074` n `229`; crypto_major avg `-0.0606` n `8`; equity avg `0.153` n `91`; fx avg `-0.0047` n `6`; index avg `0.0157` n `25`; metal avg `0.0246` n `20`; unknown avg `0.0181` n `766`
- 1h: commodity avg `0.0419` n `12`; crypto_alt avg `0.1045` n `229`; crypto_major avg `0.174` n `8`; equity avg `0.4432` n `91`; fx avg `0.0023` n `6`; index avg `0.0583` n `25`; metal avg `0.0319` n `20`; unknown avg `0.0082` n `766`
- 4h: commodity avg `-0.0571` n `12`; crypto_alt avg `0.3336` n `229`; crypto_major avg `0.4563` n `8`; equity avg `-0.0611` n `91`; fx avg `0.0109` n `6`; index avg `0.0062` n `25`; metal avg `-0.1507` n `20`; unknown avg `1.119` n `765`
- 24h: commodity avg `-0.9034` n `12`; crypto_alt avg `1.0099` n `229`; crypto_major avg `1.4428` n `8`; equity avg `0.484` n `91`; fx avg `-0.1348` n `6`; index avg `0.2543` n `25`; metal avg `0.1349` n `20`; unknown avg `0.0409` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
