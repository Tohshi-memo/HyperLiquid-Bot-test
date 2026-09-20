# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T04:07:25.675730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3636` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0261` n `12`; crypto_alt avg `0.0142` n `234`; crypto_major avg `-0.0039` n `8`; equity avg `-0.0192` n `140`; fx avg `0.0002` n `6`; index avg `0.004` n `26`; metal avg `-0.0026` n `20`; unknown avg `78.8705` n `935`
- 1h: commodity avg `0.0088` n `12`; crypto_alt avg `0.0778` n `234`; crypto_major avg `0.0294` n `8`; equity avg `0.0019` n `140`; fx avg `-0.0067` n `6`; index avg `0.0012` n `26`; metal avg `0.0119` n `20`; unknown avg `58.834` n `935`
- 4h: commodity avg `0.1995` n `12`; crypto_alt avg `-1.3343` n `234`; crypto_major avg `-1.4295` n `8`; equity avg `-0.342` n `140`; fx avg `0.0084` n `6`; index avg `-0.0659` n `26`; metal avg `-0.025` n `20`; unknown avg `5.9994` n `935`
- 24h: commodity avg `0.2263` n `12`; crypto_alt avg `-0.8803` n `234`; crypto_major avg `-2.0544` n `8`; equity avg `-0.2511` n `140`; fx avg `-0.0582` n `6`; index avg `-0.0453` n `26`; metal avg `-0.0114` n `20`; unknown avg `6.0983` n `826`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
