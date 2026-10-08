# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T17:53:05.302222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.7435` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.7307` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.5377` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.0232` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1379` n `13`; crypto_alt avg `-0.338` n `235`; crypto_major avg `-0.2889` n `8`; equity avg `-0.0189` n `150`; fx avg `0.0024` n `6`; index avg `-0.0178` n `26`; metal avg `-0.03` n `20`; unknown avg `-0.3273` n `1077`
- 1h: commodity avg `0.1872` n `13`; crypto_alt avg `-1.276` n `235`; crypto_major avg `-1.0083` n `8`; equity avg `-0.4454` n `150`; fx avg `-0.0006` n `6`; index avg `-0.0949` n `26`; metal avg `0.0497` n `20`; unknown avg `-0.2942` n `1075`
- 4h: commodity avg `-0.086` n `13`; crypto_alt avg `-5.0291` n `235`; crypto_major avg `-3.8167` n `8`; equity avg `-1.7935` n `150`; fx avg `-0.0136` n `6`; index avg `-0.279` n `26`; metal avg `-0.0732` n `20`; unknown avg `0.7849` n `1021`
- 24h: commodity avg `1.2056` n `13`; crypto_alt avg `-4.584` n `235`; crypto_major avg `-5.335` n `8`; equity avg `-3.3533` n `150`; fx avg `0.0638` n `6`; index avg `-0.4718` n `26`; metal avg `-0.0987` n `20`; unknown avg `23.6512` n `991`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
