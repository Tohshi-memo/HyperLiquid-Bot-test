# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T03:22:36.699874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.743` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.4052` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.2708` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-2.1219` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-2.0118` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `1.9927` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.7188` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0225` n `13`; crypto_alt avg `-1.1252` n `239`; crypto_major avg `-1.2621` n `8`; equity avg `-0.3955` n `162`; fx avg `0.0054` n `6`; index avg `-0.0615` n `27`; metal avg `0.0111` n `20`; unknown avg `3.2395` n `1260`
- 1h: commodity avg `-0.0677` n `13`; crypto_alt avg `-1.9328` n `239`; crypto_major avg `-2.0795` n `8`; equity avg `-0.8593` n `162`; fx avg `-0.0146` n `6`; index avg `-0.0868` n `27`; metal avg `0.0424` n `20`; unknown avg `3.9881` n `1258`
- 4h: commodity avg `-0.1689` n `13`; crypto_alt avg `-2.0907` n `239`; crypto_major avg `-2.4397` n `8`; equity avg `-0.7209` n `162`; fx avg `-0.016` n `6`; index avg `-0.0345` n `27`; metal avg `0.3033` n `20`; unknown avg `3.4643` n `1251`
- 24h: commodity avg `0.8275` n `13`; crypto_alt avg `-2.6663` n `239`; crypto_major avg `-3.9689` n `8`; equity avg `-1.3234` n `162`; fx avg `-0.0172` n `6`; index avg `-0.0044` n `27`; metal avg `-0.3402` n `20`; unknown avg `50.9302` n `1119`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
