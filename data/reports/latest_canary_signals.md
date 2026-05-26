# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T20:37:16.441762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5586` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3293` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0287` n `12`; crypto_alt avg `-0.1296` n `228`; crypto_major avg `-0.0835` n `8`; equity avg `0.0145` n `67`; fx avg `-0.0004` n `6`; index avg `0.0319` n `23`; metal avg `0.0092` n `18`; unknown avg `0.905` n `418`
- 1h: commodity avg `0.0379` n `12`; crypto_alt avg `0.07` n `228`; crypto_major avg `-0.169` n `8`; equity avg `0.0508` n `67`; fx avg `0.0156` n `6`; index avg `0.06` n `23`; metal avg `0.1651` n `18`; unknown avg `0.6105` n `418`
- 4h: commodity avg `-0.3016` n `12`; crypto_alt avg `-1.1679` n `228`; crypto_major avg `-1.2265` n `8`; equity avg `-0.1458` n `67`; fx avg `0.0341` n `6`; index avg `0.1028` n `23`; metal avg `0.3321` n `18`; unknown avg `0.3099` n `418`
- 24h: commodity avg `0.8452` n `12`; crypto_alt avg `-2.0599` n `228`; crypto_major avg `-1.5876` n `8`; equity avg `-0.4726` n `67`; fx avg `-0.0792` n `6`; index avg `0.4253` n `23`; metal avg `-0.8846` n `18`; unknown avg `1.024` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.173`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
