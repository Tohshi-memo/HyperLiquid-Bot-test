# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T21:52:45.823199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2113` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.7567` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `0.094` n `228`; crypto_major avg `-0.0131` n `8`; equity avg `0.131` n `86`; fx avg `-0.0317` n `6`; index avg `0.0058` n `23`; metal avg `0.0206` n `20`; unknown avg `1.61` n `764`
- 1h: commodity avg `0.0194` n `12`; crypto_alt avg `0.1439` n `228`; crypto_major avg `0.0161` n `8`; equity avg `0.0228` n `86`; fx avg `-0.0464` n `6`; index avg `0.0428` n `23`; metal avg `0.0519` n `20`; unknown avg `-0.8275` n `764`
- 4h: commodity avg `-0.1044` n `12`; crypto_alt avg `3.204` n `228`; crypto_major avg `3.1069` n `8`; equity avg `2.709` n `86`; fx avg `-0.0532` n `6`; index avg `0.6738` n `23`; metal avg `0.3502` n `20`; unknown avg `9.168` n `764`
- 24h: commodity avg `-0.528` n `12`; crypto_alt avg `-2.4799` n `228`; crypto_major avg `-1.9216` n `8`; equity avg `4.2139` n `86`; fx avg `0.0081` n `6`; index avg `0.5818` n `23`; metal avg `-1.6487` n `20`; unknown avg `-0.7772` n `724`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
