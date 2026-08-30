# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T22:52:42.204860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2515` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.8804` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8341` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.542` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0222` n `12`; crypto_alt avg `-0.0543` n `231`; crypto_major avg `-0.026` n `8`; equity avg `-0.0224` n `128`; fx avg `0.0012` n `6`; index avg `-0.0069` n `26`; metal avg `0.0242` n `20`; unknown avg `-0.1809` n `793`
- 1h: commodity avg `-0.2041` n `12`; crypto_alt avg `-0.5791` n `231`; crypto_major avg `-0.6103` n `8`; equity avg `-0.265` n `128`; fx avg `-0.0054` n `6`; index avg `-0.0789` n `26`; metal avg `-0.0535` n `20`; unknown avg `0.9278` n `791`
- 4h: commodity avg `0.2449` n `12`; crypto_alt avg `-1.6496` n `231`; crypto_major avg `-2.0066` n `8`; equity avg `-0.4646` n `128`; fx avg `-0.0062` n `6`; index avg `-0.1262` n `26`; metal avg `-0.1725` n `20`; unknown avg `0.9654` n `791`
- 24h: commodity avg `0.297` n `12`; crypto_alt avg `0.3308` n `231`; crypto_major avg `-0.7943` n `8`; equity avg `-0.2707` n `128`; fx avg `0.0342` n `6`; index avg `-0.0943` n `26`; metal avg `-0.0663` n `20`; unknown avg `-0.1147` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
