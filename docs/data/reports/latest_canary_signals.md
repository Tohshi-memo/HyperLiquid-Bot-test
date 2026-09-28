# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T17:07:32.919475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0248` n `12`; crypto_alt avg `-0.4876` n `234`; crypto_major avg `-0.2282` n `8`; equity avg `-0.1233` n `141`; fx avg `0.0123` n `6`; index avg `-0.0162` n `26`; metal avg `0.0045` n `20`; unknown avg `1.5201` n `960`
- 1h: commodity avg `-0.1782` n `12`; crypto_alt avg `0.0734` n `234`; crypto_major avg `0.0703` n `8`; equity avg `0.1742` n `141`; fx avg `0.014` n `6`; index avg `0.0567` n `26`; metal avg `0.0703` n `20`; unknown avg `16.2356` n `960`
- 4h: commodity avg `-0.1985` n `12`; crypto_alt avg `-1.2716` n `234`; crypto_major avg `-0.5348` n `8`; equity avg `-0.7661` n `141`; fx avg `0.0435` n `6`; index avg `-0.112` n `26`; metal avg `-0.069` n `20`; unknown avg `86.2018` n `904`
- 24h: commodity avg `-0.3157` n `12`; crypto_alt avg `-3.3609` n `234`; crypto_major avg `-1.5927` n `8`; equity avg `-3.1867` n `141`; fx avg `0.0416` n `6`; index avg `-0.2872` n `26`; metal avg `-1.0279` n `20`; unknown avg `21.0676` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1834`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
