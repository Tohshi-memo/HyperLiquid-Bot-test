# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T01:22:24.801951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.468` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.0787` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.001` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0019` n `13`; crypto_alt avg `-0.4836` n `239`; crypto_major avg `-0.6521` n `8`; equity avg `-0.4972` n `158`; fx avg `0.0052` n `6`; index avg `-0.0477` n `27`; metal avg `0.0197` n `20`; unknown avg `0.0094` n `1260`
- 1h: commodity avg `0.0006` n `13`; crypto_alt avg `0.38` n `239`; crypto_major avg `0.0549` n `8`; equity avg `0.1109` n `158`; fx avg `0.0437` n `6`; index avg `0.0734` n `27`; metal avg `0.2769` n `20`; unknown avg `0.8821` n `1254`
- 4h: commodity avg `-0.0572` n `13`; crypto_alt avg `-0.9383` n `239`; crypto_major avg `-2.0582` n `8`; equity avg `-0.6876` n `158`; fx avg `-0.0402` n `6`; index avg `0.0205` n `27`; metal avg `0.4098` n `20`; unknown avg `1.3914` n `1208`
- 24h: commodity avg `-0.1074` n `13`; crypto_alt avg `-2.2572` n `239`; crypto_major avg `-2.5104` n `8`; equity avg `-0.7131` n `158`; fx avg `-0.0047` n `6`; index avg `-0.0508` n `27`; metal avg `0.3903` n `20`; unknown avg `0.2278` n `998`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
