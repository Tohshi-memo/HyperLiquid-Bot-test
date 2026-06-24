# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T15:07:27.909987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3891` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0143` n `12`; crypto_alt avg `-0.3023` n `228`; crypto_major avg `-0.4063` n `8`; equity avg `-0.07` n `86`; fx avg `0.0177` n `6`; index avg `-0.014` n `23`; metal avg `-0.0659` n `20`; unknown avg `-0.1553` n `764`
- 1h: commodity avg `0.0204` n `12`; crypto_alt avg `-0.2344` n `228`; crypto_major avg `-0.5434` n `8`; equity avg `0.3258` n `86`; fx avg `-0.0262` n `6`; index avg `0.0874` n `23`; metal avg `-0.2208` n `20`; unknown avg `-0.2141` n `764`
- 4h: commodity avg `-0.4359` n `12`; crypto_alt avg `-0.9748` n `228`; crypto_major avg `-1.3721` n `8`; equity avg `-1.0692` n `86`; fx avg `-0.0473` n `6`; index avg `0.017` n `23`; metal avg `-0.8044` n `20`; unknown avg `0.0718` n `764`
- 24h: commodity avg `-0.7667` n `12`; crypto_alt avg `-1.5249` n `228`; crypto_major avg `-1.6412` n `8`; equity avg `2.7369` n `86`; fx avg `0.003` n `6`; index avg `0.1055` n `23`; metal avg `-1.6216` n `20`; unknown avg `-0.4601` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
