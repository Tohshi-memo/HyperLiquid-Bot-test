# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T11:37:30.672623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.1714` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8555` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0597` n `12`; crypto_alt avg `0.0661` n `228`; crypto_major avg `0.0507` n `8`; equity avg `0.0219` n `86`; fx avg `-0.0135` n `6`; index avg `-0.0056` n `23`; metal avg `-0.0193` n `20`; unknown avg `0.0548` n `765`
- 1h: commodity avg `0.1371` n `12`; crypto_alt avg `-0.3147` n `228`; crypto_major avg `-0.2383` n `8`; equity avg `0.1013` n `86`; fx avg `-0.0045` n `6`; index avg `0.0161` n `23`; metal avg `0.038` n `20`; unknown avg `0.0008` n `765`
- 4h: commodity avg `-0.0285` n `12`; crypto_alt avg `-1.475` n `228`; crypto_major avg `-1.9332` n `8`; equity avg `-0.4574` n `86`; fx avg `0.021` n `6`; index avg `-0.0777` n `23`; metal avg `0.2382` n `20`; unknown avg `-0.0377` n `765`
- 24h: commodity avg `0.1171` n `12`; crypto_alt avg `-1.9365` n `228`; crypto_major avg `-1.9594` n `8`; equity avg `-4.0374` n `86`; fx avg `0.0579` n `6`; index avg `-0.5779` n `23`; metal avg `0.7912` n `20`; unknown avg `0.7169` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2664`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1778`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
