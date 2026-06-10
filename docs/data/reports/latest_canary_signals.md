# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T20:22:38.627531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1794` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0097` n `12`; crypto_alt avg `0.3315` n `228`; crypto_major avg `0.261` n `8`; equity avg `0.2742` n `74`; fx avg `-0.0033` n `6`; index avg `0.048` n `23`; metal avg `0.0054` n `18`; unknown avg `0.0463` n `550`
- 1h: commodity avg `0.1242` n `12`; crypto_alt avg `-0.1398` n `228`; crypto_major avg `0.1874` n `8`; equity avg `-0.1135` n `74`; fx avg `-0.02` n `6`; index avg `-0.1712` n `23`; metal avg `-0.4018` n `18`; unknown avg `-0.1346` n `550`
- 4h: commodity avg `-0.2935` n `12`; crypto_alt avg `-2.2467` n `228`; crypto_major avg `-2.1501` n `8`; equity avg `-1.6225` n `74`; fx avg `-0.0172` n `6`; index avg `-0.9707` n `23`; metal avg `-1.375` n `18`; unknown avg `4.7427` n `548`
- 24h: commodity avg `1.3546` n `12`; crypto_alt avg `-2.0581` n `228`; crypto_major avg `-2.3849` n `8`; equity avg `-2.0681` n `74`; fx avg `-0.009` n `6`; index avg `-1.59` n `23`; metal avg `-2.5128` n `18`; unknown avg `-0.5094` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
