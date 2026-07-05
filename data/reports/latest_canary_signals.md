# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T01:52:25.771232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1632` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `0.0944` n `229`; crypto_major avg `0.0616` n `8`; equity avg `0.0356` n `88`; fx avg `0.0023` n `6`; index avg `0.0297` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.0941` n `765`
- 1h: commodity avg `0.0017` n `12`; crypto_alt avg `-0.417` n `229`; crypto_major avg `-0.4108` n `8`; equity avg `0.0359` n `88`; fx avg `0.0064` n `6`; index avg `-0.0008` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.0517` n `763`
- 4h: commodity avg `0.0392` n `12`; crypto_alt avg `-1.1444` n `229`; crypto_major avg `-1.1596` n `8`; equity avg `0.0221` n `88`; fx avg `0.0202` n `6`; index avg `0.0036` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.3409` n `763`
- 24h: commodity avg `0.0212` n `12`; crypto_alt avg `-0.0771` n `229`; crypto_major avg `-0.0876` n `8`; equity avg `0.289` n `88`; fx avg `0.0058` n `6`; index avg `0.0416` n `25`; metal avg `0.1237` n `20`; unknown avg `-0.7866` n `739`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
