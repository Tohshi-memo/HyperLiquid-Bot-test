# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T19:22:15.129246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.0075` n `228`; crypto_major avg `0.0381` n `8`; equity avg `0.0561` n `65`; fx avg `0.0006` n `5`; index avg `-0.001` n `23`; metal avg `-0.0546` n `18`; unknown avg `0.0554` n `384`
- 1h: commodity avg `0.0533` n `12`; crypto_alt avg `0.6192` n `228`; crypto_major avg `0.9187` n `8`; equity avg `0.197` n `65`; fx avg `0.0006` n `5`; index avg `-0.0052` n `23`; metal avg `-0.053` n `18`; unknown avg `1.141` n `384`
- 4h: commodity avg `0.1123` n `12`; crypto_alt avg `0.0198` n `228`; crypto_major avg `0.7947` n `8`; equity avg `0.1861` n `65`; fx avg `0.011` n `5`; index avg `0.029` n `23`; metal avg `-0.113` n `18`; unknown avg `1.0497` n `384`
- 24h: commodity avg `1.8735` n `12`; crypto_alt avg `-9.2949` n `228`; crypto_major avg `-1.6218` n `8`; equity avg `-2.4247` n `65`; fx avg `-0.1549` n `5`; index avg `-1.5858` n `23`; metal avg `-5.9422` n `18`; unknown avg `551.0168` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
