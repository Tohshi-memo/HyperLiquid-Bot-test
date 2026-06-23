# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T08:52:30.285330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7211` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.4137` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.3186` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.2236` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0285` n `12`; crypto_alt avg `0.2009` n `228`; crypto_major avg `-0.0163` n `8`; equity avg `0.0594` n `86`; fx avg `0.0031` n `6`; index avg `-0.0002` n `23`; metal avg `0.0353` n `20`; unknown avg `0.3811` n `764`
- 1h: commodity avg `0.1007` n `12`; crypto_alt avg `-1.0905` n `228`; crypto_major avg `-1.2713` n `8`; equity avg `-0.3846` n `86`; fx avg `-0.0316` n `6`; index avg `-0.0477` n `23`; metal avg `0.0479` n `20`; unknown avg `-0.1187` n `764`
- 4h: commodity avg `-0.023` n `12`; crypto_alt avg `-2.848` n `228`; crypto_major avg `-2.7441` n `8`; equity avg `-1.4011` n `86`; fx avg `-0.0268` n `6`; index avg `-0.3304` n `23`; metal avg `-0.4255` n `20`; unknown avg `-0.7468` n `604`
- 24h: commodity avg `-0.5745` n `12`; crypto_alt avg `-4.0521` n `228`; crypto_major avg `-4.0557` n `8`; equity avg `-4.4981` n `85`; fx avg `-0.068` n `6`; index avg `-0.8261` n `23`; metal avg `-1.489` n `18`; unknown avg `0.7584` n `583`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
