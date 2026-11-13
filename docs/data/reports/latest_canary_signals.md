# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T06:22:30.033702+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0201` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.9201` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.9192` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0509` n `13`; crypto_alt avg `0.9078` n `239`; crypto_major avg `0.7482` n `8`; equity avg `0.2374` n `162`; fx avg `0.015` n `6`; index avg `0.0168` n `27`; metal avg `0.019` n `20`; unknown avg `0.4524` n `1258`
- 1h: commodity avg `0.0017` n `13`; crypto_alt avg `0.8577` n `239`; crypto_major avg `0.2038` n `8`; equity avg `-0.0607` n `162`; fx avg `0.0372` n `6`; index avg `-0.0017` n `27`; metal avg `-0.1355` n `20`; unknown avg `162.617` n `1230`
- 4h: commodity avg `-0.0707` n `13`; crypto_alt avg `-1.2247` n `239`; crypto_major avg `-2.0908` n `8`; equity avg `-1.5549` n `162`; fx avg `0.0376` n `6`; index avg `-0.1716` n `27`; metal avg `-0.1707` n `20`; unknown avg `0.7846` n `1216`
- 24h: commodity avg `0.6642` n `13`; crypto_alt avg `-1.7538` n `239`; crypto_major avg `-3.7264` n `8`; equity avg `-1.2593` n `162`; fx avg `0.0574` n `6`; index avg `-0.0176` n `27`; metal avg `-0.5783` n `20`; unknown avg `98.8387` n `1131`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
