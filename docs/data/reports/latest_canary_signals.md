# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T22:52:34.527811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0214` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0121` n `12`; crypto_alt avg `0.1056` n `228`; crypto_major avg `0.1193` n `8`; equity avg `-0.0065` n `86`; fx avg `-0.005` n `6`; index avg `0.0083` n `23`; metal avg `-0.0274` n `20`; unknown avg `0.0467` n `716`
- 1h: commodity avg `0.0301` n `12`; crypto_alt avg `-0.7206` n `228`; crypto_major avg `-0.392` n `8`; equity avg `-0.2106` n `86`; fx avg `0.0126` n `6`; index avg `-0.0231` n `23`; metal avg `-0.053` n `20`; unknown avg `-0.1625` n `716`
- 4h: commodity avg `0.0448` n `12`; crypto_alt avg `-1.2402` n `228`; crypto_major avg `-1.0073` n `8`; equity avg `-0.2791` n `86`; fx avg `-0.0016` n `6`; index avg `0.0141` n `23`; metal avg `-0.0435` n `20`; unknown avg `0.3689` n `708`
- 24h: commodity avg `-0.8252` n `12`; crypto_alt avg `-0.8539` n `228`; crypto_major avg `-0.4213` n `8`; equity avg `-0.631` n `85`; fx avg `0.0814` n `6`; index avg `0.1594` n `23`; metal avg `0.2744` n `18`; unknown avg `0.3672` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
