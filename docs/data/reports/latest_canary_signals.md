# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T15:52:30.783198+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `3.2304` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-3.0998` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.685` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.938` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.3643` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `-0.4201` n `228`; crypto_major avg `-0.4054` n `8`; equity avg `-0.0208` n `86`; fx avg `0.0031` n `6`; index avg `-0.0225` n `23`; metal avg `0.0314` n `20`; unknown avg `-0.1511` n `764`
- 1h: commodity avg `0.1574` n `12`; crypto_alt avg `-1.2029` n `228`; crypto_major avg `-1.406` n `8`; equity avg `-0.1327` n `86`; fx avg `0.0427` n `6`; index avg `-0.0417` n `23`; metal avg `0.054` n `20`; unknown avg `-0.3173` n `764`
- 4h: commodity avg `-0.1885` n `12`; crypto_alt avg `-2.6263` n `228`; crypto_major avg `-3.2883` n `8`; equity avg `-1.3503` n `86`; fx avg `-0.0135` n `6`; index avg `-0.0579` n `23`; metal avg `-0.6033` n `20`; unknown avg `0.2574` n `764`
- 24h: commodity avg `-0.5671` n `12`; crypto_alt avg `-2.1047` n `228`; crypto_major avg `-2.341` n `8`; equity avg `2.8356` n `86`; fx avg `0.0548` n `6`; index avg `0.1293` n `23`; metal avg `-1.5735` n `20`; unknown avg `-0.1884` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
