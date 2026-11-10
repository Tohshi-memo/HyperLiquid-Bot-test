# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T15:52:33.992766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2969` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.2702` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.1749` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `-1.6665` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.5688` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1278` n `13`; crypto_alt avg `-0.4624` n `239`; crypto_major avg `-0.5358` n `8`; equity avg `-0.6025` n `160`; fx avg `-0.0203` n `6`; index avg `-0.0734` n `27`; metal avg `-0.0556` n `20`; unknown avg `18.9487` n `1262`
- 1h: commodity avg `0.0273` n `13`; crypto_alt avg `-1.4596` n `239`; crypto_major avg `-1.6284` n `8`; equity avg `-0.5719` n `160`; fx avg `-0.0807` n `6`; index avg `-0.0596` n `27`; metal avg `0.0381` n `20`; unknown avg `-0.1229` n `1256`
- 4h: commodity avg `-0.0722` n `13`; crypto_alt avg `-0.921` n `239`; crypto_major avg `-2.3691` n `8`; equity avg `-0.9781` n `160`; fx avg `-0.0738` n `6`; index avg `-0.0989` n `27`; metal avg `-0.1942` n `20`; unknown avg `1.3212` n `1250`
- 24h: commodity avg `-0.6429` n `13`; crypto_alt avg `-2.5675` n `239`; crypto_major avg `-4.2431` n `8`; equity avg `-1.5339` n `160`; fx avg `-0.1006` n `6`; index avg `-0.1137` n `27`; metal avg `-0.4317` n `20`; unknown avg `0.8677` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2328`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
