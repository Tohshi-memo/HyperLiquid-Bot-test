# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T01:22:26.722741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0943` n `13`; crypto_alt avg `-0.2776` n `236`; crypto_major avg `-0.1654` n `8`; equity avg `-0.0134` n `151`; fx avg `0.0193` n `6`; index avg `-0.0174` n `26`; metal avg `0.0635` n `20`; unknown avg `0.7483` n `1136`
- 1h: commodity avg `-0.2132` n `13`; crypto_alt avg `-0.7722` n `236`; crypto_major avg `-0.4571` n `8`; equity avg `-0.2743` n `151`; fx avg `0.073` n `6`; index avg `-0.099` n `26`; metal avg `0.0986` n `20`; unknown avg `1.6402` n `1134`
- 4h: commodity avg `-0.2779` n `13`; crypto_alt avg `-0.4156` n `236`; crypto_major avg `-0.1053` n `8`; equity avg `-1.3472` n `151`; fx avg `0.2141` n `6`; index avg `-0.3816` n `26`; metal avg `0.2814` n `20`; unknown avg `1.0726` n `1048`
- 24h: commodity avg `-0.5555` n `13`; crypto_alt avg `-3.1195` n `236`; crypto_major avg `-2.4569` n `8`; equity avg `-5.7227` n `151`; fx avg `0.0442` n `6`; index avg `-0.9221` n `26`; metal avg `-0.4821` n `20`; unknown avg `1394.358` n `890`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1064`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1023`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0997`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0939`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0917`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0873`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0832`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0735`, n `666`, weak_sample_signal
