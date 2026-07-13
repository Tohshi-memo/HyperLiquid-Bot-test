# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T10:42:06.581304+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0696` n `12`; crypto_alt avg `-0.0279` n `230`; crypto_major avg `-0.0992` n `8`; equity avg `-0.1079` n `92`; fx avg `0.0155` n `6`; index avg `-0.0564` n `25`; metal avg `-0.0692` n `20`; unknown avg `0.0056` n `766`
- 1h: commodity avg `0.2313` n `12`; crypto_alt avg `-0.0088` n `230`; crypto_major avg `-0.3117` n `8`; equity avg `-0.1907` n `92`; fx avg `-0.03` n `6`; index avg `-0.0853` n `25`; metal avg `-0.1168` n `20`; unknown avg `-0.022` n `766`
- 4h: commodity avg `-0.1156` n `12`; crypto_alt avg `0.3085` n `230`; crypto_major avg `0.0269` n `8`; equity avg `0.5388` n `92`; fx avg `-0.0737` n `6`; index avg `0.0744` n `25`; metal avg `0.1087` n `20`; unknown avg `-0.0285` n `766`
- 24h: commodity avg `-0.1494` n `12`; crypto_alt avg `-0.9779` n `230`; crypto_major avg `-1.1652` n `8`; equity avg `-2.0309` n `92`; fx avg `-0.0692` n `6`; index avg `-0.4629` n `25`; metal avg `-0.2813` n `20`; unknown avg `-0.0851` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
