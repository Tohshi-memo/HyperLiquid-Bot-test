# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T11:22:28.621879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7488` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4731` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0131` n `12`; crypto_alt avg `-0.1677` n `228`; crypto_major avg `-0.2565` n `8`; equity avg `-0.0569` n `74`; fx avg `0.014` n `6`; index avg `0.0253` n `23`; metal avg `0.0974` n `18`; unknown avg `-0.3038` n `547`
- 1h: commodity avg `-0.0387` n `12`; crypto_alt avg `0.0162` n `228`; crypto_major avg `-0.226` n `8`; equity avg `0.1114` n `74`; fx avg `0.044` n `6`; index avg `0.0813` n `23`; metal avg `0.1495` n `18`; unknown avg `-0.1781` n `547`
- 4h: commodity avg `-0.1781` n `12`; crypto_alt avg `-0.9519` n `228`; crypto_major avg `-1.202` n `8`; equity avg `0.0122` n `74`; fx avg `0.193` n `6`; index avg `0.2711` n `23`; metal avg `0.5468` n `18`; unknown avg `-0.16` n `547`
- 24h: commodity avg `-0.3439` n `12`; crypto_alt avg `-1.6855` n `228`; crypto_major avg `-0.9398` n `8`; equity avg `1.5075` n `74`; fx avg `0.1046` n `6`; index avg `0.8264` n `23`; metal avg `0.3489` n `18`; unknown avg `-3.1286` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
