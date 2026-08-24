# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T20:13:58.553609+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4217` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0484` n `12`; crypto_alt avg `0.1027` n `231`; crypto_major avg `0.1731` n `8`; equity avg `0.0354` n `122`; fx avg `-0.0023` n `6`; index avg `0.0009` n `25`; metal avg `-0.003` n `20`; unknown avg `0.0186` n `794`
- 1h: commodity avg `-0.1074` n `12`; crypto_alt avg `0.2546` n `231`; crypto_major avg `0.2272` n `8`; equity avg `-0.299` n `122`; fx avg `-0.0021` n `6`; index avg `-0.0427` n `25`; metal avg `0.0529` n `20`; unknown avg `-0.1658` n `794`
- 4h: commodity avg `-0.035` n `12`; crypto_alt avg `-1.3398` n `231`; crypto_major avg `-1.4583` n `8`; equity avg `-0.4253` n `122`; fx avg `-0.0097` n `6`; index avg `-0.0366` n `25`; metal avg `-0.0825` n `20`; unknown avg `-0.027` n `793`
- 24h: commodity avg `-0.2422` n `12`; crypto_alt avg `-1.4437` n `231`; crypto_major avg `-0.5333` n `8`; equity avg `-2.8521` n `122`; fx avg `-0.1033` n `6`; index avg `-0.3657` n `25`; metal avg `0.1143` n `20`; unknown avg `1.7693` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
