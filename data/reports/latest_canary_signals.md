# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T23:07:49.078521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3603` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.2799` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.1648` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0489` n `13`; crypto_alt avg `0.3615` n `239`; crypto_major avg `0.4844` n `8`; equity avg `0.3996` n `158`; fx avg `0.0226` n `6`; index avg `0.0992` n `27`; metal avg `0.1359` n `20`; unknown avg `1.1812` n `1246`
- 1h: commodity avg `-0.0373` n `13`; crypto_alt avg `0.7868` n `239`; crypto_major avg `0.6424` n `8`; equity avg `0.3989` n `158`; fx avg `0.0345` n `6`; index avg `0.0694` n `27`; metal avg `0.1501` n `20`; unknown avg `1.0578` n `1228`
- 4h: commodity avg `0.1221` n `13`; crypto_alt avg `-1.9005` n `239`; crypto_major avg `-2.2382` n `8`; equity avg `-0.8207` n `158`; fx avg `-0.0121` n `6`; index avg `-0.0734` n `27`; metal avg `0.0417` n `20`; unknown avg `1.2763` n `1172`
- 24h: commodity avg `-0.0304` n `13`; crypto_alt avg `-3.094` n `239`; crypto_major avg `-2.3254` n `8`; equity avg `-0.3785` n `158`; fx avg `0.0543` n `6`; index avg `-0.0506` n `27`; metal avg `0.0197` n `20`; unknown avg `-0.2067` n `1002`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
