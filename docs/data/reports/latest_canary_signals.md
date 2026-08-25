# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T20:52:56.281402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6532` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.6434` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6311` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.2143` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0674` n `12`; crypto_alt avg `-0.6537` n `231`; crypto_major avg `-0.6186` n `8`; equity avg `-0.1324` n `122`; fx avg `-0.0152` n `6`; index avg `-0.0091` n `25`; metal avg `-0.0223` n `20`; unknown avg `-0.133` n `795`
- 1h: commodity avg `-0.1136` n `12`; crypto_alt avg `-1.188` n `231`; crypto_major avg `-1.1815` n `8`; equity avg `-0.0489` n `122`; fx avg `0.0016` n `6`; index avg `0.0328` n `25`; metal avg `-0.05` n `20`; unknown avg `-0.3355` n `795`
- 4h: commodity avg `-0.1732` n `12`; crypto_alt avg `-1.9115` n `231`; crypto_major avg `-1.5862` n `8`; equity avg `0.067` n `122`; fx avg `0.0018` n `6`; index avg `0.0449` n `25`; metal avg `0.0572` n `20`; unknown avg `-0.4502` n `795`
- 24h: commodity avg `-0.6961` n `12`; crypto_alt avg `-2.1928` n `231`; crypto_major avg `-0.8001` n `8`; equity avg `2.008` n `122`; fx avg `0.0399` n `6`; index avg `0.2735` n `25`; metal avg `-0.0134` n `20`; unknown avg `-0.5674` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
