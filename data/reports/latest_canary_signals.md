# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T08:22:25.382034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.2207` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0152` n `12`; crypto_alt avg `-0.6163` n `231`; crypto_major avg `-0.7049` n `8`; equity avg `0.028` n `122`; fx avg `0.0032` n `6`; index avg `0.0185` n `25`; metal avg `-0.0429` n `20`; unknown avg `-0.2844` n `793`
- 1h: commodity avg `0.1122` n `12`; crypto_alt avg `-0.7553` n `231`; crypto_major avg `-1.223` n `8`; equity avg `-0.073` n `122`; fx avg `0.0005` n `6`; index avg `-0.0023` n `25`; metal avg `-0.0978` n `20`; unknown avg `-0.2508` n `793`
- 4h: commodity avg `0.0982` n `12`; crypto_alt avg `-0.8345` n `231`; crypto_major avg `-0.9783` n `8`; equity avg `-0.3104` n `122`; fx avg `0.0344` n `6`; index avg `-0.0398` n `25`; metal avg `0.0156` n `20`; unknown avg `-0.3952` n `777`
- 24h: commodity avg `-0.2073` n `12`; crypto_alt avg `2.0594` n `231`; crypto_major avg `0.117` n `8`; equity avg `-1.2996` n `122`; fx avg `-0.1048` n `6`; index avg `-0.1172` n `25`; metal avg `0.1204` n `20`; unknown avg `5.8705` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
