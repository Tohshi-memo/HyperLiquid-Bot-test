# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T17:52:36.755640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.8758` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-4.1185` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.712` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `1.7099` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.0142` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0285` n `13`; crypto_alt avg `-0.2281` n `239`; crypto_major avg `-0.2915` n `8`; equity avg `-0.3636` n `158`; fx avg `0.0087` n `6`; index avg `-0.0386` n `27`; metal avg `-0.0392` n `20`; unknown avg `-0.2763` n `1256`
- 1h: commodity avg `0.1277` n `13`; crypto_alt avg `-0.9797` n `239`; crypto_major avg `-1.2303` n `8`; equity avg `-1.841` n `158`; fx avg `0.014` n `6`; index avg `-0.2161` n `27`; metal avg `-0.17` n `20`; unknown avg `-0.9452` n `1250`
- 4h: commodity avg `0.43` n `13`; crypto_alt avg `-4.6714` n `239`; crypto_major avg `-4.4458` n `8`; equity avg `-6.1557` n `158`; fx avg `0.1055` n `6`; index avg `-0.7338` n `27`; metal avg `-0.3273` n `20`; unknown avg `8.0941` n `1246`
- 24h: commodity avg `0.7232` n `13`; crypto_alt avg `-5.6228` n `239`; crypto_major avg `-5.4091` n `8`; equity avg `-8.5096` n `158`; fx avg `0.1204` n `6`; index avg `-1.0984` n `27`; metal avg `0.2304` n `20`; unknown avg `218.376` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2273`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.18`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1742`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
