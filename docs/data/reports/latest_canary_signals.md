# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T21:42:28.997744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `0.0935` n `231`; crypto_major avg `-0.0234` n `8`; equity avg `-0.0034` n `122`; fx avg `0.0141` n `6`; index avg `-0.0022` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.0193` n `794`
- 1h: commodity avg `0.0505` n `12`; crypto_alt avg `0.2104` n `231`; crypto_major avg `0.0468` n `8`; equity avg `0.076` n `122`; fx avg `-0.0124` n `6`; index avg `0.0074` n `25`; metal avg `0.0173` n `20`; unknown avg `-0.0643` n `794`
- 4h: commodity avg `-0.0453` n `12`; crypto_alt avg `0.8712` n `231`; crypto_major avg `0.7226` n `8`; equity avg `-0.0588` n `122`; fx avg `-0.0071` n `6`; index avg `0.0139` n `25`; metal avg `0.0442` n `20`; unknown avg `-0.501` n `794`
- 24h: commodity avg `-0.2034` n `12`; crypto_alt avg `-1.6838` n `231`; crypto_major avg `-0.9056` n `8`; equity avg `-2.8264` n `122`; fx avg `-0.0481` n `6`; index avg `-0.3654` n `25`; metal avg `0.114` n `20`; unknown avg `0.7905` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.047`, n `668`, weak_sample_signal
