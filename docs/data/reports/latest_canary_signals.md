# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T17:52:28.607327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5421` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7762` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5687` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0954` n `13`; crypto_alt avg `0.3428` n `239`; crypto_major avg `0.3681` n `8`; equity avg `0.2608` n `160`; fx avg `0.0028` n `6`; index avg `0.0218` n `27`; metal avg `0.0611` n `20`; unknown avg `0.5469` n `1262`
- 1h: commodity avg `-0.0201` n `13`; crypto_alt avg `0.0669` n `239`; crypto_major avg `0.1997` n `8`; equity avg `-0.2461` n `160`; fx avg `0.0174` n `6`; index avg `-0.0579` n `27`; metal avg `0.0071` n `20`; unknown avg `18.9364` n `1256`
- 4h: commodity avg `0.6768` n `13`; crypto_alt avg `-1.2645` n `239`; crypto_major avg `-1.8653` n `8`; equity avg `-0.388` n `160`; fx avg `-0.0729` n `6`; index avg `-0.0891` n `27`; metal avg `-0.2966` n `20`; unknown avg `-0.0338` n `1250`
- 24h: commodity avg `-0.1843` n `13`; crypto_alt avg `-1.8829` n `239`; crypto_major avg `-3.3309` n `8`; equity avg `-2.1643` n `160`; fx avg `-0.1121` n `6`; index avg `-0.2362` n `27`; metal avg `-0.454` n `20`; unknown avg `0.4301` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.245`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
