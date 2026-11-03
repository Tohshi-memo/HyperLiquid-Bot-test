# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T11:22:35.938880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0855` n `13`; crypto_alt avg `0.1081` n `239`; crypto_major avg `-0.1635` n `8`; equity avg `-0.2046` n `157`; fx avg `0.0072` n `6`; index avg `-0.0302` n `27`; metal avg `0.0061` n `20`; unknown avg `0.054` n `1254`
- 1h: commodity avg `0.181` n `13`; crypto_alt avg `0.5913` n `239`; crypto_major avg `0.1568` n `8`; equity avg `-0.0994` n `157`; fx avg `0.0065` n `6`; index avg `-0.0321` n `27`; metal avg `0.0096` n `20`; unknown avg `0.0913` n `1228`
- 4h: commodity avg `0.2042` n `13`; crypto_alt avg `1.1506` n `239`; crypto_major avg `0.5274` n `8`; equity avg `1.0968` n `157`; fx avg `0.0647` n `6`; index avg `0.1107` n `27`; metal avg `-0.0699` n `20`; unknown avg `0.7141` n `1202`
- 24h: commodity avg `-0.1119` n `13`; crypto_alt avg `-1.1691` n `238`; crypto_major avg `-0.7898` n `8`; equity avg `-3.5255` n `157`; fx avg `0.0227` n `6`; index avg `-0.2584` n `27`; metal avg `-0.4671` n `20`; unknown avg `4.0292` n `1021`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
