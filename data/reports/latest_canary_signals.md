# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T16:37:31.960611+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0201` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.9874` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.969` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0326` n `12`; crypto_alt avg `-0.4438` n `228`; crypto_major avg `-0.3819` n `8`; equity avg `-0.3996` n `86`; fx avg `0.0183` n `6`; index avg `-0.0436` n `23`; metal avg `0.1181` n `20`; unknown avg `-0.1976` n `764`
- 1h: commodity avg `0.0747` n `12`; crypto_alt avg `-0.5175` n `228`; crypto_major avg `-0.4545` n `8`; equity avg `-0.5083` n `86`; fx avg `0.0169` n `6`; index avg `-0.0602` n `23`; metal avg `0.0484` n `20`; unknown avg `0.2782` n `764`
- 4h: commodity avg `-0.0411` n `12`; crypto_alt avg `-2.5926` n `228`; crypto_major avg `-3.0612` n `8`; equity avg `-1.5772` n `86`; fx avg `0.0122` n `6`; index avg `-0.0738` n `23`; metal avg `-0.0922` n `20`; unknown avg `0.9451` n `764`
- 24h: commodity avg `-0.3377` n `12`; crypto_alt avg `-2.5799` n `228`; crypto_major avg `-2.8602` n `8`; equity avg `2.0336` n `86`; fx avg `0.0645` n `6`; index avg `0.0312` n `23`; metal avg `-1.5778` n `20`; unknown avg `0.2794` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
