# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T18:22:27.367340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0341` n `12`; crypto_alt avg `0.0562` n `229`; crypto_major avg `0.1477` n `8`; equity avg `-0.0174` n `91`; fx avg `-0.0108` n `6`; index avg `-0.0113` n `25`; metal avg `0.026` n `20`; unknown avg `-0.0761` n `763`
- 1h: commodity avg `-0.0988` n `12`; crypto_alt avg `-0.1994` n `229`; crypto_major avg `0.0777` n `8`; equity avg `0.0476` n `91`; fx avg `-0.0143` n `6`; index avg `0.0113` n `25`; metal avg `0.0528` n `20`; unknown avg `-0.095` n `763`
- 4h: commodity avg `0.0665` n `12`; crypto_alt avg `0.6573` n `229`; crypto_major avg `1.3022` n `8`; equity avg `0.9915` n `91`; fx avg `-0.0498` n `6`; index avg `0.1746` n `25`; metal avg `0.0009` n `20`; unknown avg `0.0192` n `755`
- 24h: commodity avg `0.5486` n `12`; crypto_alt avg `-0.9876` n `229`; crypto_major avg `-0.0643` n `8`; equity avg `-2.6406` n `91`; fx avg `-0.2493` n `6`; index avg `-0.4872` n `25`; metal avg `-0.1845` n `20`; unknown avg `-0.3814` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
