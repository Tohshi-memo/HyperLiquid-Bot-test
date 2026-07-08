# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T02:07:27.060644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8102` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.2334` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0243` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0468` n `12`; crypto_alt avg `-0.335` n `229`; crypto_major avg `-0.3723` n `8`; equity avg `-0.141` n `91`; fx avg `0.0006` n `6`; index avg `-0.1151` n `25`; metal avg `0.1181` n `20`; unknown avg `-0.177` n `763`
- 1h: commodity avg `0.042` n `12`; crypto_alt avg `-1.3193` n `229`; crypto_major avg `-1.1946` n `8`; equity avg `-0.2925` n `91`; fx avg `-0.059` n `6`; index avg `-0.1703` n `25`; metal avg `0.1748` n `20`; unknown avg `0.037` n `763`
- 4h: commodity avg `-0.02` n `12`; crypto_alt avg `-0.9768` n `229`; crypto_major avg `-1.236` n `8`; equity avg `0.5742` n `91`; fx avg `0.0009` n `6`; index avg `-0.0026` n `25`; metal avg `0.1009` n `20`; unknown avg `-0.2833` n `763`
- 24h: commodity avg `0.8239` n `12`; crypto_alt avg `-3.3792` n `229`; crypto_major avg `-2.6622` n `8`; equity avg `-2.0281` n `91`; fx avg `-0.2164` n `6`; index avg `-0.3281` n `25`; metal avg `-0.3912` n `20`; unknown avg `-0.4169` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
