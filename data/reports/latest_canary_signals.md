# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T20:07:29.414139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3231` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0365` n `12`; crypto_alt avg `0.1195` n `231`; crypto_major avg `0.277` n `8`; equity avg `0.0588` n `122`; fx avg `-0.003` n `6`; index avg `0.004` n `25`; metal avg `0.0138` n `20`; unknown avg `0.0196` n `794`
- 1h: commodity avg `-0.0955` n `12`; crypto_alt avg `0.2714` n `231`; crypto_major avg `0.3313` n `8`; equity avg `-0.2758` n `122`; fx avg `-0.0028` n `6`; index avg `-0.0397` n `25`; metal avg `0.0697` n `20`; unknown avg `-0.1483` n `794`
- 4h: commodity avg `-0.023` n `12`; crypto_alt avg `-1.3237` n `231`; crypto_major avg `-1.3567` n `8`; equity avg `-0.402` n `122`; fx avg `-0.0104` n `6`; index avg `-0.0336` n `25`; metal avg `-0.0657` n `20`; unknown avg `-0.0426` n `793`
- 24h: commodity avg `-0.2301` n `12`; crypto_alt avg `-1.4273` n `231`; crypto_major avg `-0.4309` n `8`; equity avg `-2.8299` n `122`; fx avg `-0.104` n `6`; index avg `-0.3626` n `25`; metal avg `0.1312` n `20`; unknown avg `1.7897` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
