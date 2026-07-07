# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T12:07:38.925035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0894` n `12`; crypto_alt avg `0.3759` n `229`; crypto_major avg `0.5012` n `8`; equity avg `0.3341` n `91`; fx avg `-0.0083` n `6`; index avg `0.1059` n `25`; metal avg `0.0985` n `20`; unknown avg `0.0122` n `763`
- 1h: commodity avg `-0.3125` n `12`; crypto_alt avg `0.5512` n `229`; crypto_major avg `0.7898` n `8`; equity avg `0.3207` n `91`; fx avg `0.0107` n `6`; index avg `0.107` n `25`; metal avg `0.3112` n `20`; unknown avg `0.335` n `763`
- 4h: commodity avg `-0.2241` n `12`; crypto_alt avg `0.8372` n `229`; crypto_major avg `0.912` n `8`; equity avg `0.0442` n `91`; fx avg `-0.0896` n `6`; index avg `0.0229` n `25`; metal avg `0.383` n `20`; unknown avg `-0.0176` n `757`
- 24h: commodity avg `0.0684` n `12`; crypto_alt avg `2.7131` n `229`; crypto_major avg `1.8436` n `8`; equity avg `-1.2329` n `90`; fx avg `-0.1467` n `6`; index avg `-0.3571` n `25`; metal avg `-0.0222` n `20`; unknown avg `-0.1064` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
