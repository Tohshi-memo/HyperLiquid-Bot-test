# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T16:37:35.969085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.6503` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.5011` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.8859` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.071` n `13`; crypto_alt avg `-0.217` n `239`; crypto_major avg `-0.239` n `8`; equity avg `0.029` n `158`; fx avg `0.0067` n `6`; index avg `0.005` n `27`; metal avg `0.0521` n `20`; unknown avg `1.4738` n `1256`
- 1h: commodity avg `-0.0146` n `13`; crypto_alt avg `-0.1441` n `239`; crypto_major avg `-0.1436` n `8`; equity avg `0.2779` n `158`; fx avg `0.0127` n `6`; index avg `-0.028` n `27`; metal avg `0.1238` n `20`; unknown avg `1.5373` n `1246`
- 4h: commodity avg `0.2444` n `13`; crypto_alt avg `-3.6088` n `239`; crypto_major avg `-3.4059` n `8`; equity avg `-4.7125` n `158`; fx avg `0.0769` n `6`; index avg `-0.52` n `27`; metal avg `0.0952` n `20`; unknown avg `6.3583` n `1243`
- 24h: commodity avg `0.2952` n `13`; crypto_alt avg `-5.3935` n `239`; crypto_major avg `-4.7737` n `8`; equity avg `-6.0188` n `158`; fx avg `0.0943` n `6`; index avg `-0.7761` n `27`; metal avg `0.5501` n `20`; unknown avg `44.5399` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2382`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1793`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
