# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T15:37:33.654596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.3387` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.7944` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.4041` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.5685` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-2.1967` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.1245` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `1.7165` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0092` n `13`; crypto_alt avg `-0.0149` n `239`; crypto_major avg `0.1859` n `8`; equity avg `0.1473` n `158`; fx avg `0.0067` n `6`; index avg `-0.0094` n `27`; metal avg `-0.0029` n `20`; unknown avg `1.3554` n `1256`
- 1h: commodity avg `0.1282` n `13`; crypto_alt avg `-2.9294` n `239`; crypto_major avg `-2.4403` n `8`; equity avg `-2.9002` n `158`; fx avg `0.0719` n `6`; index avg `-0.3158` n `27`; metal avg `-0.2436` n `20`; unknown avg `3.6747` n `1250`
- 4h: commodity avg `0.3669` n `13`; crypto_alt avg `-4.3963` n `239`; crypto_major avg `-3.9718` n `8`; equity avg `-5.6883` n `158`; fx avg `0.0978` n `6`; index avg `-0.5677` n `27`; metal avg `-0.1774` n `20`; unknown avg `6.8295` n `1245`
- 24h: commodity avg `-0.7207` n `13`; crypto_alt avg `-5.7795` n `239`; crypto_major avg `-4.9121` n `8`; equity avg `-7.6437` n `158`; fx avg `0.0639` n `6`; index avg `-0.8659` n `27`; metal avg `0.5124` n `20`; unknown avg `27.9117` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2373`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.189`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
