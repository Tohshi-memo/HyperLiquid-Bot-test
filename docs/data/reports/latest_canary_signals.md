# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T18:45:14.887203+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3846` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `-0.3344` n `230`; crypto_major avg `-0.3544` n `8`; equity avg `-0.0204` n `102`; fx avg `0.0021` n `6`; index avg `-0.006` n `25`; metal avg `-0.0077` n `20`; unknown avg `-0.072` n `782`
- 1h: commodity avg `-0.0661` n `12`; crypto_alt avg `-0.8213` n `230`; crypto_major avg `-0.7854` n `8`; equity avg `-0.1436` n `102`; fx avg `-0.0055` n `6`; index avg `-0.0188` n `25`; metal avg `-0.013` n `20`; unknown avg `1.7536` n `782`
- 4h: commodity avg `0.0796` n `12`; crypto_alt avg `-1.4394` n `230`; crypto_major avg `-1.4436` n `8`; equity avg `-0.3333` n `102`; fx avg `-0.01` n `6`; index avg `-0.059` n `25`; metal avg `-0.0152` n `20`; unknown avg `2.1905` n `782`
- 24h: commodity avg `0.5828` n `12`; crypto_alt avg `-1.3704` n `230`; crypto_major avg `-1.9724` n `8`; equity avg `-1.4058` n `102`; fx avg `-0.1553` n `6`; index avg `-0.1869` n `25`; metal avg `-0.1222` n `20`; unknown avg `4.2023` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
