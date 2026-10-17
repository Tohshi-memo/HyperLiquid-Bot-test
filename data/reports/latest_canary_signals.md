# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T12:29:43.519105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0127` n `13`; crypto_alt avg `-0.0594` n `236`; crypto_major avg `-0.0489` n `8`; equity avg `-0.0275` n `151`; fx avg `0.0163` n `6`; index avg `-0.0094` n `26`; metal avg `-0.0057` n `20`; unknown avg `2.9867` n `1193`
- 1h: commodity avg `0.0007` n `13`; crypto_alt avg `-0.341` n `236`; crypto_major avg `-0.2561` n `8`; equity avg `-0.1228` n `151`; fx avg `0.0216` n `6`; index avg `-0.0485` n `26`; metal avg `-0.0063` n `20`; unknown avg `2.9674` n `1185`
- 4h: commodity avg `0.0577` n `13`; crypto_alt avg `-0.722` n `236`; crypto_major avg `-0.5385` n `8`; equity avg `-0.0773` n `151`; fx avg `0.0165` n `6`; index avg `-0.011` n `26`; metal avg `-0.0019` n `20`; unknown avg `3.1088` n `1183`
- 24h: commodity avg `0.4373` n `13`; crypto_alt avg `-3.004` n `236`; crypto_major avg `-1.9025` n `8`; equity avg `-3.4493` n `151`; fx avg `0.0329` n `6`; index avg `-0.581` n `26`; metal avg `-0.2165` n `20`; unknown avg `10.9836` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1815`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1478`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0695`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
