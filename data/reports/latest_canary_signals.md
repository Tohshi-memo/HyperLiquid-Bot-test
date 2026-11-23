# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T18:22:32.256445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `3.6018` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.3554` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.2442` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.5246` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0481` n `13`; crypto_alt avg `-0.1362` n `239`; crypto_major avg `-0.2416` n `8`; equity avg `0.0573` n `166`; fx avg `0.0074` n `6`; index avg `-0.0022` n `27`; metal avg `-0.0091` n `20`; unknown avg `0.2076` n `1264`
- 1h: commodity avg `0.0128` n `13`; crypto_alt avg `-0.4663` n `239`; crypto_major avg `-0.8056` n `8`; equity avg `0.0419` n `166`; fx avg `-0.0178` n `6`; index avg `-0.0032` n `27`; metal avg `-0.0664` n `20`; unknown avg `159.5032` n `1264`
- 4h: commodity avg `-0.3998` n `13`; crypto_alt avg `-2.3317` n `239`; crypto_major avg `-3.644` n `8`; equity avg `-1.1194` n `166`; fx avg `-0.151` n `6`; index avg `-0.0422` n `27`; metal avg `-0.2886` n `20`; unknown avg `207.4171` n `1256`
- 24h: commodity avg `-1.3219` n `13`; crypto_alt avg `2.6267` n `239`; crypto_major avg `2.3315` n `8`; equity avg `6.2113` n `166`; fx avg `-0.0881` n `6`; index avg `0.5637` n `27`; metal avg `0.6636` n `20`; unknown avg `245.1361` n `1060`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
