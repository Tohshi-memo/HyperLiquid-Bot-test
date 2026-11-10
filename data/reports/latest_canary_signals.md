# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T17:22:35.554197+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7928` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.2272` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.0267` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1542` n `13`; crypto_alt avg `0.5578` n `239`; crypto_major avg `0.4174` n `8`; equity avg `0.1399` n `160`; fx avg `-0.0013` n `6`; index avg `0.0152` n `27`; metal avg `-0.0243` n `20`; unknown avg `19.0163` n `1262`
- 1h: commodity avg `-0.0212` n `13`; crypto_alt avg `-0.7676` n `239`; crypto_major avg `-0.2902` n `8`; equity avg `-0.8113` n `160`; fx avg `-0.001` n `6`; index avg `-0.0877` n `27`; metal avg `-0.032` n `20`; unknown avg `18.3414` n `1256`
- 4h: commodity avg `0.4079` n `13`; crypto_alt avg `-1.5691` n `239`; crypto_major avg `-2.3849` n `8`; equity avg `-1.2516` n `160`; fx avg `-0.0885` n `6`; index avg `-0.1577` n `27`; metal avg `-0.3582` n `20`; unknown avg `-0.129` n `1250`
- 24h: commodity avg `-0.3159` n `13`; crypto_alt avg `-1.9891` n `239`; crypto_major avg `-3.2918` n `8`; equity avg `-2.1579` n `160`; fx avg `-0.1267` n `6`; index avg `-0.193` n `27`; metal avg `-0.5056` n `20`; unknown avg `0.3999` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2416`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
