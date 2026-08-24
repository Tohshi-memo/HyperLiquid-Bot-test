# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T19:52:24.956335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0861` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0257` n `12`; crypto_alt avg `-0.3057` n `231`; crypto_major avg `-0.4024` n `8`; equity avg `-0.159` n `122`; fx avg `-0.0024` n `6`; index avg `-0.0269` n `25`; metal avg `0.0308` n `20`; unknown avg `0.1842` n `794`
- 1h: commodity avg `-0.0783` n `12`; crypto_alt avg `-0.1573` n `231`; crypto_major avg `-0.0827` n `8`; equity avg `-0.4712` n `122`; fx avg `0.0021` n `6`; index avg `-0.0552` n `25`; metal avg `0.0702` n `20`; unknown avg `-0.1581` n `794`
- 4h: commodity avg `0.0135` n `12`; crypto_alt avg `-1.0608` n `231`; crypto_major avg `-1.1274` n `8`; equity avg `-0.4825` n `122`; fx avg `-0.021` n `6`; index avg `-0.0413` n `25`; metal avg `-0.0537` n `20`; unknown avg `-0.4229` n `793`
- 24h: commodity avg `-0.1909` n `12`; crypto_alt avg `-1.7745` n `231`; crypto_major avg `-0.9021` n `8`; equity avg `-2.901` n `122`; fx avg `-0.0825` n `6`; index avg `-0.3705` n `25`; metal avg `0.112` n `20`; unknown avg `2.2492` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
