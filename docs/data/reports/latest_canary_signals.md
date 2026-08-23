# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T04:51:05.088891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.693` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.6649` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.6338` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.5675` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0096` n `12`; crypto_alt avg `-0.4048` n `230`; crypto_major avg `-0.418` n `8`; equity avg `-0.054` n `121`; fx avg `-0.0065` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0107` n `20`; unknown avg `-0.2261` n `794`
- 1h: commodity avg `-0.0112` n `12`; crypto_alt avg `-0.7412` n `230`; crypto_major avg `-0.8218` n `8`; equity avg `-0.0767` n `121`; fx avg `-0.0039` n `6`; index avg `-0.0014` n `25`; metal avg `-0.0223` n `20`; unknown avg `-0.3602` n `794`
- 4h: commodity avg `-0.0439` n `12`; crypto_alt avg `-3.5379` n `230`; crypto_major avg `-2.6777` n `8`; equity avg `-0.1102` n `121`; fx avg `0.0082` n `6`; index avg `0.0153` n `25`; metal avg `-0.0128` n `20`; unknown avg `7.0614` n `794`
- 24h: commodity avg `0.0051` n `12`; crypto_alt avg `-9.3512` n `230`; crypto_major avg `-5.8252` n `8`; equity avg `-0.3424` n `121`; fx avg `0.0887` n `6`; index avg `-0.0325` n `25`; metal avg `-0.0193` n `20`; unknown avg `1.9593` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
