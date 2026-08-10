# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T15:37:39.255272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0047` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0477` n `12`; crypto_alt avg `-0.0049` n `230`; crypto_major avg `-0.0862` n `8`; equity avg `-0.1243` n `113`; fx avg `-0.0007` n `6`; index avg `-0.0217` n `25`; metal avg `0.0034` n `20`; unknown avg `0.0177` n `784`
- 1h: commodity avg `0.1359` n `12`; crypto_alt avg `-0.6343` n `230`; crypto_major avg `-0.7698` n `8`; equity avg `-0.644` n `113`; fx avg `-0.009` n `6`; index avg `-0.0837` n `25`; metal avg `0.0229` n `20`; unknown avg `1.8054` n `784`
- 4h: commodity avg `0.494` n `12`; crypto_alt avg `-0.7947` n `230`; crypto_major avg `-1.0753` n `8`; equity avg `-0.9419` n `113`; fx avg `0.0323` n `6`; index avg `-0.0706` n `25`; metal avg `0.1253` n `20`; unknown avg `1.5757` n `784`
- 24h: commodity avg `1.1077` n `12`; crypto_alt avg `-0.5176` n `230`; crypto_major avg `-1.5235` n `8`; equity avg `-1.3747` n `113`; fx avg `0.2521` n `6`; index avg `-0.0582` n `25`; metal avg `-0.0858` n `20`; unknown avg `103.4827` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1641`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
