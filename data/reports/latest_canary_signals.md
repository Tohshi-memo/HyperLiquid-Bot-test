# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T15:14:17.849331+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3507` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0414` n `12`; crypto_alt avg `-0.3931` n `228`; crypto_major avg `-0.3972` n `8`; equity avg `-0.0659` n `86`; fx avg `0.0294` n `6`; index avg `-0.0438` n `23`; metal avg `-0.0689` n `20`; unknown avg `-0.1244` n `764`
- 1h: commodity avg `0.0475` n `12`; crypto_alt avg `-0.325` n `228`; crypto_major avg `-0.5343` n `8`; equity avg `0.33` n `86`; fx avg `-0.0145` n `6`; index avg `0.0574` n `23`; metal avg `-0.2238` n `20`; unknown avg `-0.1801` n `764`
- 4h: commodity avg `-0.409` n `12`; crypto_alt avg `-1.0646` n `228`; crypto_major avg `-1.3634` n `8`; equity avg `-1.0652` n `86`; fx avg `-0.0355` n `6`; index avg `-0.0127` n `23`; metal avg `-0.8071` n `20`; unknown avg `0.1109` n `764`
- 24h: commodity avg `-0.74` n `12`; crypto_alt avg `-1.6143` n `228`; crypto_major avg `-1.6326` n `8`; equity avg `2.7385` n `86`; fx avg `0.0147` n `6`; index avg `0.0754` n `23`; metal avg `-1.6242` n `20`; unknown avg `-0.4375` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
