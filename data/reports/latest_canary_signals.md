# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T03:52:25.847730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1524` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `0.0752` n `229`; crypto_major avg `0.071` n `8`; equity avg `0.0028` n `88`; fx avg `0.0021` n `6`; index avg `0.0177` n `25`; metal avg `0.0022` n `20`; unknown avg `0.0526` n `765`
- 1h: commodity avg `-0.0125` n `12`; crypto_alt avg `0.1622` n `229`; crypto_major avg `0.2521` n `8`; equity avg `0.0581` n `88`; fx avg `-0.0021` n `6`; index avg `-0.0011` n `25`; metal avg `0.0056` n `20`; unknown avg `0.0076` n `765`
- 4h: commodity avg `0.028` n `12`; crypto_alt avg `-0.9751` n `229`; crypto_major avg `-1.1545` n `8`; equity avg `0.0741` n `88`; fx avg `-0.0006` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0376` n `20`; unknown avg `-0.4418` n `763`
- 24h: commodity avg `0.0389` n `12`; crypto_alt avg `-0.9095` n `229`; crypto_major avg `-0.9654` n `8`; equity avg `0.1847` n `88`; fx avg `-0.0023` n `6`; index avg `0.0336` n `25`; metal avg `0.084` n `20`; unknown avg `-0.9328` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
