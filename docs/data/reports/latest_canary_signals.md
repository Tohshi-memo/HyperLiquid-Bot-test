# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T18:37:29.180859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.419` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.1322` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.59` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.775` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0266` n `12`; crypto_alt avg `-0.2658` n `231`; crypto_major avg `-0.3252` n `8`; equity avg `-0.107` n `127`; fx avg `0.0005` n `6`; index avg `-0.0107` n `26`; metal avg `-0.0516` n `20`; unknown avg `5.7316` n `793`
- 1h: commodity avg `-0.0286` n `12`; crypto_alt avg `-0.8896` n `231`; crypto_major avg `-0.8645` n `8`; equity avg `-0.09` n `127`; fx avg `0.0022` n `6`; index avg `-0.0121` n `26`; metal avg `-0.1745` n `20`; unknown avg `5.2672` n `793`
- 4h: commodity avg `0.0506` n `12`; crypto_alt avg `-3.2865` n `231`; crypto_major avg `-3.3684` n `8`; equity avg `-1.5934` n `127`; fx avg `-0.0004` n `6`; index avg `-0.2362` n `26`; metal avg `-0.7784` n `20`; unknown avg `6.0886` n `793`
- 24h: commodity avg `-0.2375` n `12`; crypto_alt avg `-3.7771` n `231`; crypto_major avg `-3.8193` n `8`; equity avg `-2.0249` n `127`; fx avg `-0.1035` n `6`; index avg `-0.0805` n `26`; metal avg `-0.3261` n `20`; unknown avg `-0.5205` n `760`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
