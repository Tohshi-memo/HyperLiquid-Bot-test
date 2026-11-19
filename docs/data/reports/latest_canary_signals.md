# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T15:52:41.027695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.3633` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.2192` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0322` n `13`; crypto_alt avg `-0.2744` n `239`; crypto_major avg `-0.3355` n `8`; equity avg `0.2523` n `165`; fx avg `0.0518` n `6`; index avg `0.0143` n `27`; metal avg `-0.0332` n `20`; unknown avg `20.107` n `1265`
- 1h: commodity avg `-0.2909` n `13`; crypto_alt avg `-1.3843` n `239`; crypto_major avg `-1.6601` n `8`; equity avg `-2.4451` n `165`; fx avg `0.0124` n `6`; index avg `-0.2968` n `27`; metal avg `-0.2776` n `20`; unknown avg `5.4422` n `1263`
- 4h: commodity avg `0.0516` n `13`; crypto_alt avg `-1.6009` n `239`; crypto_major avg `-1.5741` n `8`; equity avg `-2.3409` n `165`; fx avg `0.0097` n `6`; index avg `-0.3549` n `27`; metal avg `-0.415` n `20`; unknown avg `10.4545` n `1257`
- 24h: commodity avg `0.0559` n `13`; crypto_alt avg `0.0178` n `239`; crypto_major avg `0.2026` n `8`; equity avg `0.8734` n `165`; fx avg `0.0555` n `6`; index avg `0.1735` n `27`; metal avg `-0.4094` n `20`; unknown avg `5.3288` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
