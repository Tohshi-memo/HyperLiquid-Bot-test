# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T21:53:11.582043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0315` n `13`; crypto_alt avg `-0.2552` n `235`; crypto_major avg `-0.1229` n `8`; equity avg `0.0195` n `150`; fx avg `-0.0014` n `6`; index avg `-0.0014` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.1089` n `1068`
- 1h: commodity avg `-0.0298` n `13`; crypto_alt avg `-0.1503` n `235`; crypto_major avg `-0.1684` n `8`; equity avg `0.0306` n `150`; fx avg `0.0045` n `6`; index avg `0.0116` n `26`; metal avg `0.0197` n `20`; unknown avg `-0.1175` n `1060`
- 4h: commodity avg `0.3173` n `13`; crypto_alt avg `-0.609` n `235`; crypto_major avg `-0.3037` n `8`; equity avg `-0.2699` n `150`; fx avg `-0.0119` n `6`; index avg `-0.0441` n `26`; metal avg `0.0142` n `20`; unknown avg `1.301` n `998`
- 24h: commodity avg `0.3383` n `13`; crypto_alt avg `-1.628` n `235`; crypto_major avg `-1.043` n `8`; equity avg `0.4058` n `149`; fx avg `0.1131` n `6`; index avg `-0.0089` n `26`; metal avg `0.0478` n `20`; unknown avg `863.2612` n `922`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
