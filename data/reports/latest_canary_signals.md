# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T05:07:26.118826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.3166` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.2922` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.2809` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.2096` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0121` n `12`; crypto_alt avg `-0.0437` n `230`; crypto_major avg `-0.0612` n `8`; equity avg `-0.0091` n `121`; fx avg `0.0043` n `6`; index avg `-0.0008` n `25`; metal avg `0.0008` n `20`; unknown avg `-0.0835` n `794`
- 1h: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.5611` n `230`; crypto_major avg `-0.8154` n `8`; equity avg `-0.0572` n `121`; fx avg `0.0046` n `6`; index avg `-0.0022` n `25`; metal avg `-0.0083` n `20`; unknown avg `-0.2195` n `794`
- 4h: commodity avg `-0.0281` n `12`; crypto_alt avg `-3.2031` n `230`; crypto_major avg `-2.309` n `8`; equity avg `-0.0994` n `121`; fx avg `0.0061` n `6`; index avg `0.0076` n `25`; metal avg `-0.0168` n `20`; unknown avg `3.6529` n `794`
- 24h: commodity avg `0.0217` n `12`; crypto_alt avg `-3.8643` n `230`; crypto_major avg `-1.4718` n `8`; equity avg `0.4094` n `121`; fx avg `0.0945` n `6`; index avg `0.0565` n `25`; metal avg `0.2163` n `20`; unknown avg `3.6135` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
