# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T00:22:27.367057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0551` n `12`; crypto_alt avg `0.1979` n `228`; crypto_major avg `0.0414` n `8`; equity avg `0.02` n `74`; fx avg `0.0004` n `6`; index avg `0.0326` n `23`; metal avg `-0.0012` n `18`; unknown avg `-0.053` n `643`
- 1h: commodity avg `0.0424` n `12`; crypto_alt avg `0.5829` n `228`; crypto_major avg `0.2038` n `8`; equity avg `0.1186` n `74`; fx avg `0.0419` n `6`; index avg `0.1568` n `23`; metal avg `0.0516` n `18`; unknown avg `-0.1621` n `643`
- 4h: commodity avg `-0.2553` n `12`; crypto_alt avg `-0.0528` n `228`; crypto_major avg `-0.5532` n `8`; equity avg `0.2422` n `74`; fx avg `0.0578` n `6`; index avg `0.2261` n `23`; metal avg `-0.0131` n `18`; unknown avg `0.645` n `643`
- 24h: commodity avg `-0.6166` n `12`; crypto_alt avg `-0.3528` n `228`; crypto_major avg `-0.1145` n `8`; equity avg `-0.7442` n `74`; fx avg `0.0123` n `6`; index avg `0.4665` n `23`; metal avg `0.3099` n `18`; unknown avg `40.9593` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
