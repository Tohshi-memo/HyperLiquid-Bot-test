# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T22:07:28.754432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.8153` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `-2.6899` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.6392` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.6271` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `2.5082` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.4872` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-1.8177` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `-1.7828` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1914` n `13`; crypto_alt avg `-1.2765` n `239`; crypto_major avg `-1.4295` n `8`; equity avg `-0.3874` n `158`; fx avg `-0.0076` n `6`; index avg `-0.0305` n `27`; metal avg `-0.0747` n `20`; unknown avg `-0.2526` n `1248`
- 1h: commodity avg `0.1071` n `13`; crypto_alt avg `-2.4096` n `239`; crypto_major avg `-2.5828` n `8`; equity avg `-0.7651` n `158`; fx avg `-0.0271` n `6`; index avg `-0.0746` n `27`; metal avg `-0.0956` n `20`; unknown avg `0.285` n `1246`
- 4h: commodity avg `0.0817` n `13`; crypto_alt avg `-2.2993` n `239`; crypto_major avg `-2.7336` n `8`; equity avg `-0.9508` n `158`; fx avg `-0.0589` n `6`; index avg `-0.1065` n `27`; metal avg `-0.0944` n `20`; unknown avg `13.8682` n `1178`
- 24h: commodity avg `0.0131` n `13`; crypto_alt avg `-3.5826` n `239`; crypto_major avg `-2.8274` n `8`; equity avg `-0.6967` n `158`; fx avg `0.0074` n `6`; index avg `-0.1217` n `27`; metal avg `-0.1256` n `20`; unknown avg `-0.5673` n `1024`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
