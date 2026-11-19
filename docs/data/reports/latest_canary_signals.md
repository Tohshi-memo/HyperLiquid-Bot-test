# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T17:07:27.706610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0988` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7111` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.652` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1366` n `13`; crypto_alt avg `-0.52` n `239`; crypto_major avg `-0.5641` n `8`; equity avg `-1.4518` n `165`; fx avg `-0.0226` n `6`; index avg `-0.1493` n `27`; metal avg `-0.2007` n `20`; unknown avg `1.0729` n `1260`
- 1h: commodity avg `-0.1396` n `13`; crypto_alt avg `-0.8146` n `239`; crypto_major avg `-0.7314` n `8`; equity avg `-2.0224` n `165`; fx avg `-0.0432` n `6`; index avg `-0.2435` n `27`; metal avg `-0.1289` n `20`; unknown avg `13.6134` n `1263`
- 4h: commodity avg `-0.1158` n `13`; crypto_alt avg `-2.3912` n `239`; crypto_major avg `-2.2146` n `8`; equity avg `-3.6345` n `165`; fx avg `-0.0509` n `6`; index avg `-0.5035` n `27`; metal avg `-0.5626` n `20`; unknown avg `12.5948` n `1257`
- 24h: commodity avg `0.2608` n `13`; crypto_alt avg `-0.7388` n `239`; crypto_major avg `-0.2407` n `8`; equity avg `-0.9208` n `165`; fx avg `0.0024` n `6`; index avg `-0.0818` n `27`; metal avg `-0.5611` n `20`; unknown avg `3.7918` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
