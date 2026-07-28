# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T01:37:24.589643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.033` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.8454` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.822` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0332` n `12`; crypto_alt avg `0.2226` n `230`; crypto_major avg `0.238` n `8`; equity avg `0.1889` n `102`; fx avg `0.0007` n `6`; index avg `0.0264` n `25`; metal avg `0.0447` n `20`; unknown avg `0.0176` n `773`
- 1h: commodity avg `0.0071` n `12`; crypto_alt avg `-0.5394` n `230`; crypto_major avg `-0.3865` n `8`; equity avg `-0.4384` n `102`; fx avg `0.0194` n `6`; index avg `-0.0604` n `25`; metal avg `-0.1523` n `20`; unknown avg `0.2906` n `774`
- 4h: commodity avg `-0.0831` n `12`; crypto_alt avg `-2.3384` n `230`; crypto_major avg `-2.1161` n `8`; equity avg `-1.4305` n `102`; fx avg `0.0746` n `6`; index avg `-0.2707` n `25`; metal avg `-0.2941` n `20`; unknown avg `2.1018` n `774`
- 24h: commodity avg `-0.7626` n `12`; crypto_alt avg `-3.8338` n `230`; crypto_major avg `-2.9817` n `8`; equity avg `-2.115` n `102`; fx avg `-0.0489` n `6`; index avg `-0.5572` n `25`; metal avg `-0.309` n `20`; unknown avg `1161.8824` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.3494`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.3088`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1931`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
