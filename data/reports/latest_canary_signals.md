# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T04:22:18.902399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.8581` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.4445` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0524` n `12`; crypto_alt avg `-0.6364` n `228`; crypto_major avg `-0.3141` n `8`; equity avg `-0.1897` n `67`; fx avg `-0.0041` n `6`; index avg `-0.1595` n `23`; metal avg `-0.1727` n `18`; unknown avg `5.0369` n `419`
- 1h: commodity avg `0.2133` n `12`; crypto_alt avg `-2.1059` n `228`; crypto_major avg `-1.3108` n `8`; equity avg `-1.2356` n `67`; fx avg `-0.0728` n `6`; index avg `-0.5511` n `23`; metal avg `-0.3225` n `18`; unknown avg `7.2294` n `419`
- 4h: commodity avg `0.6772` n `12`; crypto_alt avg `-3.4274` n `228`; crypto_major avg `-2.1809` n `8`; equity avg `-1.843` n `67`; fx avg `-0.1092` n `6`; index avg `-0.7364` n `23`; metal avg `-1.8604` n `18`; unknown avg `-0.3488` n `419`
- 24h: commodity avg `0.3551` n `12`; crypto_alt avg `-4.3941` n `228`; crypto_major avg `-3.2687` n `8`; equity avg `-2.4707` n `67`; fx avg `-0.1117` n `6`; index avg `-1.4689` n `23`; metal avg `-2.8728` n `18`; unknown avg `-1.1949` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1793`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1724`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
