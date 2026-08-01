# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T16:26:36.013173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0876` n `12`; crypto_alt avg `0.1388` n `230`; crypto_major avg `0.0415` n `8`; equity avg `-0.0218` n `102`; fx avg `0.007` n `6`; index avg `-0.0298` n `25`; metal avg `-0.0015` n `20`; unknown avg `-0.0148` n `782`
- 1h: commodity avg `0.1003` n `12`; crypto_alt avg `0.1651` n `230`; crypto_major avg `-0.0426` n `8`; equity avg `-0.0692` n `102`; fx avg `-0.0061` n `6`; index avg `-0.016` n `25`; metal avg `-0.0153` n `20`; unknown avg `-0.0585` n `782`
- 4h: commodity avg `0.0809` n `12`; crypto_alt avg `-0.0131` n `230`; crypto_major avg `0.0245` n `8`; equity avg `-0.1847` n `102`; fx avg `0.0242` n `6`; index avg `-0.011` n `25`; metal avg `0.0092` n `20`; unknown avg `-0.1792` n `782`
- 24h: commodity avg `0.7274` n `12`; crypto_alt avg `0.3783` n `230`; crypto_major avg `-0.4492` n `8`; equity avg `-0.3236` n `102`; fx avg `-0.0649` n `6`; index avg `-0.0316` n `25`; metal avg `0.0408` n `20`; unknown avg `4.2037` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
