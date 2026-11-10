# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T16:07:50.729433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-2.1919` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_commodity_crypto_divergence: score `-2.1703` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.1271` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.1189` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.1038` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.9152` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5996` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0007` n `13`; crypto_alt avg `-0.0126` n `239`; crypto_major avg `0.0827` n `8`; equity avg `0.3613` n `160`; fx avg `-0.0057` n `6`; index avg `0.0499` n `27`; metal avg `-0.0066` n `20`; unknown avg `0.0466` n `1250`
- 1h: commodity avg `-0.0456` n `13`; crypto_alt avg `-2.1558` n `239`; crypto_major avg `-2.2375` n `8`; equity avg `-1.3905` n `160`; fx avg `-0.0683` n `6`; index avg `-0.1337` n `27`; metal avg `-0.1186` n `20`; unknown avg `-0.1636` n `1250`
- 4h: commodity avg `-0.0077` n `13`; crypto_alt avg `-0.8733` n `239`; crypto_major avg `-2.178` n `8`; equity avg `-0.5784` n `160`; fx avg `-0.0908` n `6`; index avg `-0.0509` n `27`; metal avg `-0.2628` n `20`; unknown avg `19.5362` n `1250`
- 24h: commodity avg `-0.6551` n `13`; crypto_alt avg `-2.3414` n `239`; crypto_major avg `-3.8717` n `8`; equity avg `-1.3405` n `160`; fx avg `-0.1065` n `6`; index avg `-0.0681` n `27`; metal avg `-0.5103` n `20`; unknown avg `0.9442` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2347`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
