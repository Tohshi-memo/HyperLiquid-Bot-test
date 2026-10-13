# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T11:22:26.102989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0588` n `13`; crypto_alt avg `0.309` n `235`; crypto_major avg `0.5048` n `8`; equity avg `-0.0037` n `151`; fx avg `-0.0009` n `6`; index avg `-0.0098` n `26`; metal avg `0.0196` n `20`; unknown avg `0.3111` n `1135`
- 1h: commodity avg `0.1308` n `13`; crypto_alt avg `-0.5275` n `235`; crypto_major avg `-0.0576` n `8`; equity avg `-0.4547` n `151`; fx avg `0.0183` n `6`; index avg `-0.071` n `26`; metal avg `-0.0033` n `20`; unknown avg `-0.015` n `1133`
- 4h: commodity avg `-0.0018` n `13`; crypto_alt avg `-1.6703` n `235`; crypto_major avg `-0.7389` n `8`; equity avg `-0.1021` n `151`; fx avg `-0.0071` n `6`; index avg `-0.007` n `26`; metal avg `-0.0674` n `20`; unknown avg `0.0684` n `1117`
- 24h: commodity avg `-0.0089` n `13`; crypto_alt avg `-4.2313` n `235`; crypto_major avg `-2.163` n `8`; equity avg `-3.0782` n `151`; fx avg `0.0736` n `6`; index avg `-0.3736` n `26`; metal avg `0.0029` n `20`; unknown avg `0.3455` n `989`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1718`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1685`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1572`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1465`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0735`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
