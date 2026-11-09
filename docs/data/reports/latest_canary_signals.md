# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T00:22:29.344516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.4832` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.3029` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.2342` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0565` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0139` n `13`; crypto_alt avg `0.4664` n `239`; crypto_major avg `0.3164` n `8`; equity avg `0.162` n `158`; fx avg `-0.0206` n `6`; index avg `0.024` n `27`; metal avg `0.0546` n `20`; unknown avg `0.1067` n `1262`
- 1h: commodity avg `-0.0093` n `13`; crypto_alt avg `-0.6824` n `239`; crypto_major avg `-1.1466` n `8`; equity avg `-0.6742` n `158`; fx avg `-0.0713` n `6`; index avg `-0.0901` n `27`; metal avg `0.0436` n `20`; unknown avg `2.317` n `1248`
- 4h: commodity avg `-0.0461` n `13`; crypto_alt avg `-1.4563` n `239`; crypto_major avg `-2.349` n `8`; equity avg `-1.0597` n `158`; fx avg `-0.0941` n `6`; index avg `-0.1148` n `27`; metal avg `0.1342` n `20`; unknown avg `1.3326` n `1186`
- 24h: commodity avg `-0.0746` n `13`; crypto_alt avg `-2.9684` n `239`; crypto_major avg `-2.751` n `8`; equity avg `-0.8569` n `158`; fx avg `-0.0568` n `6`; index avg `-0.1304` n `27`; metal avg `0.1113` n `20`; unknown avg `0.1638` n `1000`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
