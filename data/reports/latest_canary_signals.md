# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T14:52:31.254276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5976` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.2068` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.1756` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `1.9611` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.8762` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0639` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0198` n `13`; crypto_alt avg `-0.6937` n `239`; crypto_major avg `-0.6829` n `8`; equity avg `-1.5167` n `158`; fx avg `0.0365` n `6`; index avg `-0.132` n `27`; metal avg `-0.1957` n `20`; unknown avg `0.0689` n `1254`
- 1h: commodity avg `0.2083` n `13`; crypto_alt avg `-1.3927` n `239`; crypto_major avg `-1.3798` n `8`; equity avg `-3.3409` n `158`; fx avg `0.043` n `6`; index avg `-0.3159` n `27`; metal avg `-0.2334` n `20`; unknown avg `6.016` n `1254`
- 4h: commodity avg `0.3505` n `13`; crypto_alt avg `-2.1247` n `239`; crypto_major avg `-2.2471` n `8`; equity avg `-4.4227` n `158`; fx avg `0.0462` n `6`; index avg `-0.3709` n `27`; metal avg `-0.0403` n `20`; unknown avg `19.9611` n `1243`
- 24h: commodity avg `-0.529` n `13`; crypto_alt avg `-2.7324` n `239`; crypto_major avg `-2.1354` n `8`; equity avg `-6.6202` n `158`; fx avg `0.0024` n `6`; index avg `-0.6967` n `27`; metal avg `0.5595` n `20`; unknown avg `41.7878` n `1066`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.232`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2056`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
