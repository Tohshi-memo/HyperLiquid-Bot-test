# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T21:07:30.818849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1305` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1542` n `12`; crypto_alt avg `-0.5461` n `228`; crypto_major avg `-0.3378` n `8`; equity avg `-0.0443` n `74`; fx avg `-0.0323` n `6`; index avg `0.0622` n `23`; metal avg `0.0556` n `18`; unknown avg `-0.0708` n `550`
- 1h: commodity avg `0.2887` n `12`; crypto_alt avg `-0.6103` n `228`; crypto_major avg `-0.3847` n `8`; equity avg `-0.0941` n `74`; fx avg `-0.0324` n `6`; index avg `-0.0083` n `23`; metal avg `-0.0873` n `18`; unknown avg `-0.0361` n `550`
- 4h: commodity avg `0.018` n `12`; crypto_alt avg `-2.3439` n `228`; crypto_major avg `-1.8651` n `8`; equity avg `-1.549` n `74`; fx avg `-0.0711` n `6`; index avg `-0.7346` n `23`; metal avg `-1.3102` n `18`; unknown avg `-0.1655` n `548`
- 24h: commodity avg `1.4608` n `12`; crypto_alt avg `-3.2779` n `228`; crypto_major avg `-3.3422` n `8`; equity avg `-2.4908` n `74`; fx avg `-0.0345` n `6`; index avg `-1.7418` n `23`; metal avg `-2.6654` n `18`; unknown avg `-0.6072` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
