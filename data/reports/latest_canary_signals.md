# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T07:07:33.897061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0349` n `13`; crypto_alt avg `-0.1991` n `236`; crypto_major avg `-0.1374` n `8`; equity avg `0.0556` n `151`; fx avg `0.003` n `6`; index avg `0.0041` n `26`; metal avg `0.0211` n `20`; unknown avg `-0.0591` n `1134`
- 1h: commodity avg `0.1486` n `13`; crypto_alt avg `0.4695` n `236`; crypto_major avg `0.2844` n `8`; equity avg `-0.0806` n `151`; fx avg `-0.0181` n `6`; index avg `-0.0147` n `26`; metal avg `0.0495` n `20`; unknown avg `0.4585` n `1134`
- 4h: commodity avg `0.1276` n `13`; crypto_alt avg `0.9213` n `236`; crypto_major avg `0.3379` n `8`; equity avg `0.0551` n `151`; fx avg `-0.0866` n `6`; index avg `-0.0141` n `26`; metal avg `-0.0183` n `20`; unknown avg `0.5357` n `1102`
- 24h: commodity avg `0.0568` n `13`; crypto_alt avg `5.0393` n `236`; crypto_major avg `2.5092` n `8`; equity avg `2.5535` n `151`; fx avg `0.0321` n `6`; index avg `0.3674` n `26`; metal avg `0.4557` n `20`; unknown avg `26.6253` n `904`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.1013`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0931`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0925`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0918`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0595`, n `666`, weak_sample_signal
