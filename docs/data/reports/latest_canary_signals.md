# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T19:38:03.360663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4496` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0411` n `12`; crypto_alt avg `0.4389` n `231`; crypto_major avg `0.4239` n `8`; equity avg `-0.152` n `122`; fx avg `0.0025` n `6`; index avg `-0.0216` n `25`; metal avg `-0.0129` n `20`; unknown avg `-0.2074` n `794`
- 1h: commodity avg `0.0045` n `12`; crypto_alt avg `0.0299` n `231`; crypto_major avg `0.2825` n `8`; equity avg `-0.3354` n `122`; fx avg `0.0034` n `6`; index avg `-0.0533` n `25`; metal avg `0.0801` n `20`; unknown avg `-0.257` n `794`
- 4h: commodity avg `0.0617` n `12`; crypto_alt avg `-1.446` n `231`; crypto_major avg `-1.44` n `8`; equity avg `-0.2655` n `122`; fx avg `-0.0226` n `6`; index avg `0.0096` n `25`; metal avg `-0.233` n `20`; unknown avg `-0.34` n `793`
- 24h: commodity avg `-0.1759` n `12`; crypto_alt avg `-1.4633` n `231`; crypto_major avg `-0.4621` n `8`; equity avg `-2.7663` n `122`; fx avg `-0.1267` n `6`; index avg `-0.3429` n `25`; metal avg `0.0843` n `20`; unknown avg `2.2755` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
