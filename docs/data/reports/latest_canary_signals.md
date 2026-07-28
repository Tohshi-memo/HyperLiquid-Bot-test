# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T00:52:31.851562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1219` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.9` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8198` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0698` n `12`; crypto_alt avg `-0.1728` n `230`; crypto_major avg `-0.1889` n `8`; equity avg `-0.2927` n `102`; fx avg `0.0003` n `6`; index avg `-0.0543` n `25`; metal avg `-0.055` n `20`; unknown avg `-0.1209` n `774`
- 1h: commodity avg `-0.0338` n `12`; crypto_alt avg `-0.0009` n `230`; crypto_major avg `-0.2079` n `8`; equity avg `-0.6413` n `102`; fx avg `0.0529` n `6`; index avg `-0.1883` n `25`; metal avg `-0.1428` n `20`; unknown avg `0.007` n `774`
- 4h: commodity avg `0.0354` n `12`; crypto_alt avg `-2.1331` n `230`; crypto_major avg `-2.0865` n `8`; equity avg `-1.2027` n `102`; fx avg `0.044` n `6`; index avg `-0.2667` n `25`; metal avg `-0.1865` n `20`; unknown avg `1.2816` n `774`
- 24h: commodity avg `-0.6631` n `12`; crypto_alt avg `-3.7213` n `230`; crypto_major avg `-3.116` n `8`; equity avg `-2.6019` n `102`; fx avg `-0.0532` n `6`; index avg `-0.6933` n `25`; metal avg `-0.2724` n `20`; unknown avg `1161.7814` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.3247`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2949`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.193`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
