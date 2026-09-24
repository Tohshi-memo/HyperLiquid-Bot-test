# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T01:29:44.502599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0254` n `12`; crypto_alt avg `-0.2259` n `234`; crypto_major avg `-0.2161` n `8`; equity avg `-0.0884` n `141`; fx avg `-0.0112` n `6`; index avg `-0.0072` n `26`; metal avg `-0.0399` n `20`; unknown avg `5.3197` n `945`
- 1h: commodity avg `-0.0401` n `12`; crypto_alt avg `-0.1976` n `234`; crypto_major avg `-0.2568` n `8`; equity avg `-0.1102` n `141`; fx avg `0.0069` n `6`; index avg `0.0082` n `26`; metal avg `0.0644` n `20`; unknown avg `5.2324` n `943`
- 4h: commodity avg `-0.1847` n `12`; crypto_alt avg `0.3223` n `234`; crypto_major avg `0.3808` n `8`; equity avg `-0.1405` n `141`; fx avg `0.0067` n `6`; index avg `-0.0197` n `26`; metal avg `-0.0362` n `20`; unknown avg `4.8757` n `937`
- 24h: commodity avg `0.3027` n `12`; crypto_alt avg `-4.839` n `234`; crypto_major avg `-3.9546` n `8`; equity avg `-1.8061` n `140`; fx avg `0.0655` n `6`; index avg `-0.3359` n `26`; metal avg `-0.7059` n `20`; unknown avg `589.7039` n `821`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
