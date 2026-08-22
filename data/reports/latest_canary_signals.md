# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T05:48:13.178223+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-4.0051` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `3.9118` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-3.8973` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-3.5661` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `0.2733` n `230`; crypto_major avg `0.3515` n `8`; equity avg `0.0594` n `121`; fx avg `0.0038` n `6`; index avg `-0.0028` n `25`; metal avg `0.0358` n `20`; unknown avg `0.2972` n `794`
- 1h: commodity avg `0.0609` n `12`; crypto_alt avg `-5.082` n `230`; crypto_major avg `-3.9442` n `8`; equity avg `-0.3781` n `121`; fx avg `0.0084` n `6`; index avg `-0.0324` n `25`; metal avg `-0.0469` n `20`; unknown avg `2.0842` n `794`
- 4h: commodity avg `0.0971` n `12`; crypto_alt avg `-0.7858` n `230`; crypto_major avg `0.7627` n `8`; equity avg `-0.3476` n `121`; fx avg `0.031` n `6`; index avg `-0.0348` n `25`; metal avg `-0.0813` n `20`; unknown avg `0.4573` n `793`
- 24h: commodity avg `0.2023` n `12`; crypto_alt avg `6.6896` n `230`; crypto_major avg `6.4612` n `8`; equity avg `-0.0817` n `121`; fx avg `0.0581` n `6`; index avg `-0.025` n `25`; metal avg `0.0829` n `20`; unknown avg `2.0359` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
