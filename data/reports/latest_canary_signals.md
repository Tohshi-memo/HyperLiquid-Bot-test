# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T12:52:30.740072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.9842` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6796` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.087` n `12`; crypto_alt avg `-0.6232` n `228`; crypto_major avg `-0.5312` n `8`; equity avg `-0.2445` n `86`; fx avg `0.0176` n `6`; index avg `-0.0432` n `23`; metal avg `0.0127` n `20`; unknown avg `-0.0668` n `765`
- 1h: commodity avg `-0.2079` n `12`; crypto_alt avg `-0.1609` n `228`; crypto_major avg `-0.0903` n `8`; equity avg `-0.2257` n `86`; fx avg `0.0096` n `6`; index avg `-0.0462` n `23`; metal avg `0.0629` n `20`; unknown avg `-0.0423` n `765`
- 4h: commodity avg `-0.0131` n `12`; crypto_alt avg `-1.3358` n `228`; crypto_major avg `-1.7512` n `8`; equity avg `-0.4459` n `86`; fx avg `0.0045` n `6`; index avg `-0.0716` n `23`; metal avg `0.233` n `20`; unknown avg `-0.2247` n `765`
- 24h: commodity avg `-0.0665` n `12`; crypto_alt avg `-2.3211` n `228`; crypto_major avg `-2.6238` n `8`; equity avg `-4.6415` n `86`; fx avg `0.0563` n `6`; index avg `-0.7193` n `23`; metal avg `0.2645` n `20`; unknown avg `0.674` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.3074`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
