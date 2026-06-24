# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T16:07:32.191374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `3.1435` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-3.0606` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.748` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.66` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.1167` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0223` n `12`; crypto_alt avg `-0.0912` n `228`; crypto_major avg `-0.1175` n `8`; equity avg `-0.2654` n `86`; fx avg `-0.0086` n `6`; index avg `-0.0151` n `23`; metal avg `-0.1258` n `20`; unknown avg `0.1084` n `764`
- 1h: commodity avg `0.094` n `12`; crypto_alt avg `-0.9048` n `228`; crypto_major avg `-1.1298` n `8`; equity avg `-0.3307` n `86`; fx avg `0.0047` n `6`; index avg `-0.0131` n `23`; metal avg `-0.0031` n `20`; unknown avg `-0.2486` n `764`
- 4h: commodity avg `-0.1609` n `12`; crypto_alt avg `-2.7272` n `228`; crypto_major avg `-3.2215` n `8`; equity avg `-1.5615` n `86`; fx avg `-0.0232` n `6`; index avg `-0.078` n `23`; metal avg `-0.4735` n `20`; unknown avg `0.3119` n `764`
- 24h: commodity avg `-0.582` n `12`; crypto_alt avg `-2.723` n `228`; crypto_major avg `-3.119` n `8`; equity avg `2.1833` n `86`; fx avg `0.0452` n `6`; index avg `0.0595` n `23`; metal avg `-1.7166` n `20`; unknown avg `-0.2155` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
