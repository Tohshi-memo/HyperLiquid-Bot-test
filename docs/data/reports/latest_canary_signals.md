# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T12:52:27.563616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.1823` n `229`; crypto_major avg `-0.0813` n `8`; equity avg `0.124` n `91`; fx avg `0.0036` n `6`; index avg `0.0582` n `25`; metal avg `0.1479` n `20`; unknown avg `0.0609` n `764`
- 1h: commodity avg `-0.1464` n `12`; crypto_alt avg `-0.2077` n `229`; crypto_major avg `-0.2594` n `8`; equity avg `0.5021` n `91`; fx avg `-0.0005` n `6`; index avg `0.1256` n `25`; metal avg `0.2072` n `20`; unknown avg `0.0643` n `757`
- 4h: commodity avg `-0.3108` n `12`; crypto_alt avg `0.0775` n `229`; crypto_major avg `0.1215` n `8`; equity avg `0.7748` n `91`; fx avg `-0.0478` n `6`; index avg `0.1751` n `25`; metal avg `0.0291` n `20`; unknown avg `0.088` n `757`
- 24h: commodity avg `1.2507` n `12`; crypto_alt avg `-3.6734` n `229`; crypto_major avg `-3.2067` n `8`; equity avg `-2.0934` n `91`; fx avg `-0.0995` n `6`; index avg `-0.4616` n `25`; metal avg `-1.2474` n `20`; unknown avg `-0.4401` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
