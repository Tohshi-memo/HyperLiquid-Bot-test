# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T03:22:36.985321+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.34` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0262` n `12`; crypto_alt avg `0.1965` n `234`; crypto_major avg `0.1416` n `8`; equity avg `0.031` n `140`; fx avg `-0.0023` n `6`; index avg `-0.0021` n `26`; metal avg `-0.0002` n `20`; unknown avg `0.1683` n `943`
- 1h: commodity avg `0.0784` n `12`; crypto_alt avg `-1.3702` n `234`; crypto_major avg `-0.9086` n `8`; equity avg `-0.3855` n `140`; fx avg `-0.0098` n `6`; index avg `-0.0734` n `26`; metal avg `-0.0373` n `20`; unknown avg `4.5851` n `941`
- 4h: commodity avg `0.232` n `12`; crypto_alt avg `-1.0779` n `234`; crypto_major avg `-1.4068` n `8`; equity avg `-0.2854` n `140`; fx avg `0.0177` n `6`; index avg `-0.0668` n `26`; metal avg `-0.0286` n `20`; unknown avg `6.9962` n `919`
- 24h: commodity avg `0.1816` n `12`; crypto_alt avg `-0.8002` n `234`; crypto_major avg `-1.9453` n `8`; equity avg `-0.2156` n `140`; fx avg `-0.0556` n `6`; index avg `-0.0263` n `26`; metal avg `-0.0288` n `20`; unknown avg `5.6492` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
