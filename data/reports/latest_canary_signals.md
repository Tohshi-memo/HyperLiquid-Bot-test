# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T18:22:23.787469+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.9296` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.2194` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0174` n `12`; crypto_alt avg `0.0274` n `231`; crypto_major avg `0.1287` n `8`; equity avg `0.187` n `122`; fx avg `-0.0019` n `6`; index avg `0.044` n `25`; metal avg `0.0243` n `20`; unknown avg `-0.0749` n `794`
- 1h: commodity avg `0.0164` n `12`; crypto_alt avg `0.3937` n `231`; crypto_major avg `0.4122` n `8`; equity avg `0.2865` n `122`; fx avg `-0.0068` n `6`; index avg `0.0556` n `25`; metal avg `-0.031` n `20`; unknown avg `-0.1797` n `794`
- 4h: commodity avg `-0.1446` n `12`; crypto_alt avg `-0.6606` n `231`; crypto_major avg `-1.0923` n `8`; equity avg `0.8373` n `122`; fx avg `-0.0452` n `6`; index avg `0.1271` n `25`; metal avg `-0.1946` n `20`; unknown avg `-0.0555` n `793`
- 24h: commodity avg `-0.2375` n `12`; crypto_alt avg `-1.2424` n `231`; crypto_major avg `-0.4869` n `8`; equity avg `-2.2122` n `122`; fx avg `-0.158` n `6`; index avg `-0.2757` n `25`; metal avg `0.0722` n `20`; unknown avg `2.853` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
