# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T05:52:22.207380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-3.8584` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `3.7626` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-3.756` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-3.4399` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `0.2336` n `230`; crypto_major avg `0.5112` n `8`; equity avg `0.0812` n `121`; fx avg `-0.0007` n `6`; index avg `-0.0042` n `25`; metal avg `0.0423` n `20`; unknown avg `0.213` n `794`
- 1h: commodity avg `0.062` n `12`; crypto_alt avg `-5.1193` n `230`; crypto_major avg `-3.7964` n `8`; equity avg `-0.3565` n `121`; fx avg `0.0039` n `6`; index avg `-0.0338` n `25`; metal avg `-0.0404` n `20`; unknown avg `1.8994` n `794`
- 4h: commodity avg `0.0982` n `12`; crypto_alt avg `-0.8247` n `230`; crypto_major avg `0.9249` n `8`; equity avg `-0.3261` n `121`; fx avg `0.0266` n `6`; index avg `-0.0363` n `25`; metal avg `-0.0749` n `20`; unknown avg `0.3663` n `793`
- 24h: commodity avg `0.2035` n `12`; crypto_alt avg `6.6514` n `230`; crypto_major avg `6.6411` n `8`; equity avg `-0.06` n `121`; fx avg `0.0536` n `6`; index avg `-0.0265` n `25`; metal avg `0.0893` n `20`; unknown avg `1.986` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
