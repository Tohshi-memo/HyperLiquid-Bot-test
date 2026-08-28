# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T19:37:31.189812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3444` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0521` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5936` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0651` n `12`; crypto_alt avg `0.0934` n `231`; crypto_major avg `0.0889` n `8`; equity avg `0.0276` n `127`; fx avg `-0.0015` n `6`; index avg `-0.0069` n `26`; metal avg `0.0456` n `20`; unknown avg `0.1141` n `793`
- 1h: commodity avg `0.0605` n `12`; crypto_alt avg `0.7281` n `231`; crypto_major avg `0.5011` n `8`; equity avg `0.0018` n `127`; fx avg `-0.0066` n `6`; index avg `-0.0035` n `26`; metal avg `0.0473` n `20`; unknown avg `0.1076` n `793`
- 4h: commodity avg `0.0616` n `12`; crypto_alt avg `-2.172` n `231`; crypto_major avg `-2.2828` n `8`; equity avg `-1.2169` n `127`; fx avg `-0.0321` n `6`; index avg `-0.2307` n `26`; metal avg `-0.6892` n `20`; unknown avg `1.5246` n `793`
- 24h: commodity avg `-0.1792` n `12`; crypto_alt avg `-3.2727` n `231`; crypto_major avg `-3.7289` n `8`; equity avg `-2.2072` n `127`; fx avg `-0.1165` n `6`; index avg `-0.1439` n `26`; metal avg `-0.3556` n `20`; unknown avg `-0.69` n `760`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
