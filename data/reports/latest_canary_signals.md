# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T15:52:29.127189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1107` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.144` n `12`; crypto_alt avg `-0.1126` n `229`; crypto_major avg `-0.0264` n `8`; equity avg `-0.3013` n `91`; fx avg `0.0027` n `6`; index avg `-0.025` n `25`; metal avg `0.019` n `20`; unknown avg `-0.06` n `764`
- 1h: commodity avg `0.1812` n `12`; crypto_alt avg `-0.3117` n `229`; crypto_major avg `-0.3018` n `8`; equity avg `-0.5834` n `91`; fx avg `0.0081` n `6`; index avg `-0.0787` n `25`; metal avg `-0.1851` n `20`; unknown avg `-0.2171` n `764`
- 4h: commodity avg `0.4306` n `12`; crypto_alt avg `-0.6188` n `229`; crypto_major avg `-1.0571` n `8`; equity avg `0.4171` n `91`; fx avg `0.0574` n `6`; index avg `0.0536` n `25`; metal avg `-0.33` n `20`; unknown avg `-0.2209` n `757`
- 24h: commodity avg `1.3183` n `12`; crypto_alt avg `-4.2483` n `229`; crypto_major avg `-4.5253` n `8`; equity avg `-0.6292` n `91`; fx avg `-0.0127` n `6`; index avg `-0.3196` n `25`; metal avg `-1.506` n `20`; unknown avg `-0.6793` n `737`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
