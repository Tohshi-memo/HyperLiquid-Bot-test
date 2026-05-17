# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T23:52:16.058446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.5096` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.1234` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.0634` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.7749` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.025` n `12`; crypto_alt avg `-1.3994` n `228`; crypto_major avg `-0.899` n `8`; equity avg `0.149` n `66`; fx avg `0.0344` n `5`; index avg `-0.0353` n `23`; metal avg `0.0602` n `18`; unknown avg `1.8534` n `383`
- 1h: commodity avg `0.1734` n `12`; crypto_alt avg `-1.9194` n `228`; crypto_major avg `-1.1643` n `8`; equity avg `-0.3678` n `66`; fx avg `0.0299` n `5`; index avg `-0.2549` n `23`; metal avg `-0.1756` n `18`; unknown avg `1.4697` n `383`
- 4h: commodity avg `0.1772` n `12`; crypto_alt avg `-2.654` n `228`; crypto_major avg `-1.9462` n `8`; equity avg `0.1172` n `66`; fx avg `0.011` n `5`; index avg `-0.1713` n `23`; metal avg `0.5634` n `18`; unknown avg `0.9216` n `383`
- 24h: commodity avg `2.04` n `12`; crypto_alt avg `-11.4086` n `228`; crypto_major avg `-3.1633` n `8`; equity avg `-2.8424` n `65`; fx avg `-0.1431` n `5`; index avg `-1.7068` n `23`; metal avg `-5.4396` n `18`; unknown avg `550.9222` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
