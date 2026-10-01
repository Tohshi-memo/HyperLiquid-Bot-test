# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T11:07:40.705347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2294` n `13`; crypto_alt avg `-0.2178` n `234`; crypto_major avg `-0.0655` n `8`; equity avg `-0.136` n `142`; fx avg `0.0174` n `6`; index avg `-0.0359` n `26`; metal avg `-0.0232` n `20`; unknown avg `0.1675` n `973`
- 1h: commodity avg `-0.0877` n `13`; crypto_alt avg `0.2418` n `234`; crypto_major avg `0.4742` n `8`; equity avg `0.3214` n `142`; fx avg `0.0202` n `6`; index avg `0.086` n `26`; metal avg `0.186` n `20`; unknown avg `0.1173` n `973`
- 4h: commodity avg `0.0072` n `13`; crypto_alt avg `-1.5938` n `234`; crypto_major avg `-0.5833` n `8`; equity avg `-0.3892` n `142`; fx avg `-0.0353` n `6`; index avg `-0.0747` n `26`; metal avg `-0.1458` n `20`; unknown avg `8.1784` n `957`
- 24h: commodity avg `-0.2223` n `13`; crypto_alt avg `-0.5768` n `234`; crypto_major avg `0.1833` n `8`; equity avg `0.7452` n `142`; fx avg `0.0555` n `6`; index avg `0.2243` n `26`; metal avg `-0.1612` n `20`; unknown avg `777.1204` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1689`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
