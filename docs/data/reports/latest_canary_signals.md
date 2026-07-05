# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T01:20:58.456688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3261` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `-0.5367` n `229`; crypto_major avg `-0.4417` n `8`; equity avg `-0.042` n `88`; fx avg `0.0033` n `6`; index avg `-0.0335` n `25`; metal avg `-0.0023` n `20`; unknown avg `-0.0475` n `763`
- 1h: commodity avg `0.0081` n `12`; crypto_alt avg `-0.4674` n `229`; crypto_major avg `-0.5039` n `8`; equity avg `-0.02` n `88`; fx avg `-0.0004` n `6`; index avg `-0.0011` n `25`; metal avg `-0.001` n `20`; unknown avg `-0.1751` n `763`
- 4h: commodity avg `0.0352` n `12`; crypto_alt avg `-1.3826` n `229`; crypto_major avg `-1.3074` n `8`; equity avg `-0.0391` n `88`; fx avg `0.0145` n `6`; index avg `0.0187` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.14` n `763`
- 24h: commodity avg `0.0076` n `12`; crypto_alt avg `-0.3894` n `229`; crypto_major avg `-0.3584` n `8`; equity avg `0.2142` n `88`; fx avg `0.0036` n `6`; index avg `0.0508` n `25`; metal avg `0.1269` n `20`; unknown avg `-0.7682` n `739`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
