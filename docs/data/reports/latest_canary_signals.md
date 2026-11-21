# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T05:22:26.725711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.8193` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.7637` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.6796` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.5361` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0094` n `13`; crypto_alt avg `0.3348` n `239`; crypto_major avg `0.5492` n `8`; equity avg `0.0717` n `166`; fx avg `0.0012` n `6`; index avg `0.0071` n `27`; metal avg `0.0124` n `20`; unknown avg `-0.1496` n `1260`
- 1h: commodity avg `0.0154` n `13`; crypto_alt avg `0.8877` n `239`; crypto_major avg `1.0513` n `8`; equity avg `0.3735` n `166`; fx avg `-0.0093` n `6`; index avg `0.0612` n `27`; metal avg `0.0706` n `20`; unknown avg `477.3967` n `1256`
- 4h: commodity avg `-0.0393` n `13`; crypto_alt avg `-3.2019` n `239`; crypto_major avg `-3.8586` n `8`; equity avg `-1.3225` n `166`; fx avg `-0.0315` n `6`; index avg `-0.0949` n `27`; metal avg `-0.179` n `20`; unknown avg `293.6948` n `1242`
- 24h: commodity avg `0.2962` n `13`; crypto_alt avg `-6.2273` n `239`; crypto_major avg `-8.0101` n `8`; equity avg `-5.4019` n `166`; fx avg `-0.0433` n `6`; index avg `-0.5682` n `27`; metal avg `0.0057` n `20`; unknown avg `12.8398` n `1111`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
