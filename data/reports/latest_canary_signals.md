# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T19:07:13.840308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0109` n `12`; crypto_alt avg `0.3133` n `228`; crypto_major avg `0.4958` n `8`; equity avg `0.0687` n `65`; fx avg `-0.0017` n `5`; index avg `0.0093` n `23`; metal avg `0.0041` n `18`; unknown avg `0.9741` n `384`
- 1h: commodity avg `0.1029` n `12`; crypto_alt avg `0.2497` n `228`; crypto_major avg `0.667` n `8`; equity avg `0.128` n `65`; fx avg `-0.0013` n `5`; index avg `0.0112` n `23`; metal avg `-0.0067` n `18`; unknown avg `0.882` n `384`
- 4h: commodity avg `0.116` n `12`; crypto_alt avg `-0.0941` n `228`; crypto_major avg `0.6384` n `8`; equity avg `0.2422` n `65`; fx avg `0.0095` n `5`; index avg `0.0481` n `23`; metal avg `-0.0386` n `18`; unknown avg `0.9221` n `384`
- 24h: commodity avg `1.8743` n `12`; crypto_alt avg `-9.288` n `228`; crypto_major avg `-1.6649` n `8`; equity avg `-2.4804` n `65`; fx avg `-0.1555` n `5`; index avg `-1.5854` n `23`; metal avg `-5.8906` n `18`; unknown avg `550.9524` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
