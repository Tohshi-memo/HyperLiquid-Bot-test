# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T10:52:31.354513+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0768` n `12`; crypto_alt avg `-0.1805` n `229`; crypto_major avg `-0.1421` n `8`; equity avg `-0.0679` n `91`; fx avg `-0.0128` n `6`; index avg `-0.0615` n `25`; metal avg `-0.0665` n `20`; unknown avg `-0.0559` n `763`
- 1h: commodity avg `0.047` n `12`; crypto_alt avg `0.0903` n `229`; crypto_major avg `-0.1917` n `8`; equity avg `-0.0406` n `91`; fx avg `-0.0501` n `6`; index avg `-0.0832` n `25`; metal avg `0.024` n `20`; unknown avg `-0.0215` n `763`
- 4h: commodity avg `0.0478` n `12`; crypto_alt avg `-0.0925` n `229`; crypto_major avg `-0.3081` n `8`; equity avg `-0.3608` n `91`; fx avg `-0.1414` n `6`; index avg `-0.0958` n `25`; metal avg `0.1292` n `20`; unknown avg `-0.4321` n `757`
- 24h: commodity avg `0.462` n `12`; crypto_alt avg `0.3317` n `229`; crypto_major avg `-0.3562` n `8`; equity avg `-1.5745` n `90`; fx avg `-0.1391` n `6`; index avg `-0.4252` n `25`; metal avg `-0.3125` n `20`; unknown avg `-0.4446` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0494`, n `668`, weak_sample_signal
