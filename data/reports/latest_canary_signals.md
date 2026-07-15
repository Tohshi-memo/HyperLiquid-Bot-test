# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T12:52:31.787298+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0224` n `12`; crypto_alt avg `0.4233` n `230`; crypto_major avg `0.5524` n `8`; equity avg `0.1246` n `93`; fx avg `0.0086` n `6`; index avg `0.0243` n `25`; metal avg `0.0326` n `20`; unknown avg `0.0414` n `768`
- 1h: commodity avg `0.0409` n `12`; crypto_alt avg `0.7527` n `230`; crypto_major avg `0.7315` n `8`; equity avg `0.2101` n `93`; fx avg `0.0065` n `6`; index avg `0.0447` n `25`; metal avg `0.1806` n `20`; unknown avg `0.1225` n `767`
- 4h: commodity avg `0.0611` n `12`; crypto_alt avg `1.0037` n `230`; crypto_major avg `0.906` n `8`; equity avg `0.1193` n `93`; fx avg `0.007` n `6`; index avg `0.0062` n `25`; metal avg `0.0432` n `20`; unknown avg `0.0205` n `767`
- 24h: commodity avg `-0.1518` n `12`; crypto_alt avg `1.3954` n `230`; crypto_major avg `2.3672` n `8`; equity avg `0.7468` n `92`; fx avg `0.034` n `6`; index avg `0.2116` n `25`; metal avg `0.0954` n `20`; unknown avg `0.2068` n `738`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
