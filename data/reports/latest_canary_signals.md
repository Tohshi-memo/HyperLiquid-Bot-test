# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T17:37:44.493107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.8506` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.172` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.9399` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0098` n `13`; crypto_alt avg `-0.2708` n `239`; crypto_major avg `-0.3627` n `8`; equity avg `-0.4053` n `160`; fx avg `0.0087` n `6`; index avg `-0.0476` n `27`; metal avg `-0.0485` n `20`; unknown avg `18.9355` n `1262`
- 1h: commodity avg `-0.0455` n `13`; crypto_alt avg `-0.1786` n `239`; crypto_major avg `0.0701` n `8`; equity avg `-0.9654` n `160`; fx avg `0.0211` n `6`; index avg `-0.1169` n `27`; metal avg `-0.0395` n `20`; unknown avg `18.7987` n `1256`
- 4h: commodity avg `0.5562` n `13`; crypto_alt avg `-1.5994` n `239`; crypto_major avg `-2.2944` n `8`; equity avg `-0.7966` n `160`; fx avg `-0.0713` n `6`; index avg `-0.1224` n `27`; metal avg `-0.3545` n `20`; unknown avg `0.5007` n `1250`
- 24h: commodity avg `-0.304` n `13`; crypto_alt avg `-2.1388` n `239`; crypto_major avg `-3.6059` n `8`; equity avg `-2.5011` n `160`; fx avg `-0.1173` n `6`; index avg `-0.2677` n `27`; metal avg `-0.537` n `20`; unknown avg `0.5703` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2432`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
