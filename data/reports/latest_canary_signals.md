# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T11:07:24.806678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1734` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0555` n `12`; crypto_alt avg `-0.1049` n `228`; crypto_major avg `-0.137` n `8`; equity avg `0.1298` n `74`; fx avg `0.0112` n `6`; index avg `0.0801` n `23`; metal avg `0.033` n `18`; unknown avg `0.6602` n `547`
- 1h: commodity avg `-0.0637` n `12`; crypto_alt avg `0.1569` n `228`; crypto_major avg `-0.0103` n `8`; equity avg `0.1289` n `74`; fx avg `0.0519` n `6`; index avg `0.0352` n `23`; metal avg `0.2392` n `18`; unknown avg `0.5788` n `547`
- 4h: commodity avg `-0.1479` n `12`; crypto_alt avg `-0.6427` n `228`; crypto_major avg `-0.9356` n `8`; equity avg `-0.0383` n `74`; fx avg `0.1993` n `6`; index avg `0.2378` n `23`; metal avg `0.3674` n `18`; unknown avg `0.3012` n `547`
- 24h: commodity avg `-1.04` n `12`; crypto_alt avg `-0.8499` n `228`; crypto_major avg `0.1457` n `8`; equity avg `2.2652` n `74`; fx avg `0.0995` n `6`; index avg `1.1902` n `23`; metal avg `1.0898` n `18`; unknown avg `-2.864` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
