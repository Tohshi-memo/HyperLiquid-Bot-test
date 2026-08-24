# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T01:22:24.941971+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2937` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0894` n `12`; crypto_alt avg `-0.4023` n `231`; crypto_major avg `-0.3953` n `8`; equity avg `-0.021` n `122`; fx avg `0.0072` n `6`; index avg `0.0155` n `25`; metal avg `-0.0711` n `20`; unknown avg `0.0438` n `793`
- 1h: commodity avg `-0.2017` n `12`; crypto_alt avg `-0.3935` n `231`; crypto_major avg `-0.4445` n `8`; equity avg `0.1352` n `122`; fx avg `-0.0064` n `6`; index avg `0.0562` n `25`; metal avg `-0.0647` n `20`; unknown avg `0.2504` n `793`
- 4h: commodity avg `-0.3463` n `12`; crypto_alt avg `-2.0823` n `231`; crypto_major avg `-1.3203` n `8`; equity avg `-0.3658` n `122`; fx avg `-0.0082` n `6`; index avg `-0.0266` n `25`; metal avg `-0.0717` n `20`; unknown avg `0.7` n `793`
- 24h: commodity avg `-0.4721` n `12`; crypto_alt avg `1.5692` n `231`; crypto_major avg `-0.5104` n `8`; equity avg `0.2753` n `122`; fx avg `-0.1496` n `6`; index avg `0.076` n `25`; metal avg `0.0268` n `20`; unknown avg `5.7557` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
