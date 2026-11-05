# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T15:22:52.707276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.6247` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-4.0573` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.6735` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-3.1026` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-2.7391` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.636` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_equity_divergence: score `1.5642` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `1.5575` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0059` n `13`; crypto_alt avg `-1.3349` n `239`; crypto_major avg `-0.9072` n `8`; equity avg `-1.1887` n `158`; fx avg `0.0403` n `6`; index avg `-0.1077` n `27`; metal avg `-0.1123` n `20`; unknown avg `2.399` n `1256`
- 1h: commodity avg `0.0261` n `13`; crypto_alt avg `-3.4253` n `239`; crypto_major avg `-3.0765` n `8`; equity avg `-4.6407` n `158`; fx avg `0.042` n `6`; index avg `-0.4405` n `27`; metal avg `-0.3374` n `20`; unknown avg `4.6962` n `1252`
- 4h: commodity avg `0.402` n `13`; crypto_alt avg `-4.4379` n `239`; crypto_major avg `-4.2227` n `8`; equity avg `-5.7802` n `158`; fx avg `0.0783` n `6`; index avg `-0.5492` n `27`; metal avg `-0.1654` n `20`; unknown avg `6.1183` n `1245`
- 24h: commodity avg `-0.599` n `13`; crypto_alt avg `-5.7482` n `239`; crypto_major avg `-5.1615` n `8`; equity avg `-7.87` n `158`; fx avg `0.0496` n `6`; index avg `-0.8417` n `27`; metal avg `0.5712` n `20`; unknown avg `214.1478` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.235`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1942`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
