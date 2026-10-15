# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T09:07:32.259743+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0122` n `13`; crypto_alt avg `0.0242` n `236`; crypto_major avg `0.0446` n `8`; equity avg `0.0925` n `151`; fx avg `-0.0076` n `6`; index avg `0.0085` n `26`; metal avg `0.0396` n `20`; unknown avg `-0.0523` n `1134`
- 1h: commodity avg `0.1769` n `13`; crypto_alt avg `0.5389` n `236`; crypto_major avg `0.142` n `8`; equity avg `0.2653` n `151`; fx avg `0.036` n `6`; index avg `0.034` n `26`; metal avg `0.0235` n `20`; unknown avg `0.0854` n `1134`
- 4h: commodity avg `0.0835` n `13`; crypto_alt avg `0.0857` n `236`; crypto_major avg `0.0889` n `8`; equity avg `-0.6995` n `151`; fx avg `-0.0348` n `6`; index avg `-0.0605` n `26`; metal avg `0.1484` n `20`; unknown avg `5.5354` n `1092`
- 24h: commodity avg `-0.2516` n `13`; crypto_alt avg `-4.3482` n `236`; crypto_major avg `-2.99` n `8`; equity avg `-5.7055` n `151`; fx avg `0.0858` n `6`; index avg `-0.935` n `26`; metal avg `-0.4296` n `20`; unknown avg `2.5103` n `970`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1165`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1006`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.098`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0892`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0789`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0659`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0654`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0639`, n `666`, weak_sample_signal
