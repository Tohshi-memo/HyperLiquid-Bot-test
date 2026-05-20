# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T21:07:20.005618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1992` n `12`; crypto_alt avg `0.1164` n `228`; crypto_major avg `0.0713` n `8`; equity avg `0.0265` n `66`; fx avg `-0.0012` n `6`; index avg `0.0364` n `23`; metal avg `-0.0157` n `18`; unknown avg `0.0356` n `384`
- 1h: commodity avg `0.3572` n `12`; crypto_alt avg `0.2242` n `228`; crypto_major avg `-0.0679` n `8`; equity avg `0.0224` n `66`; fx avg `-0.0039` n `6`; index avg `-0.0684` n `23`; metal avg `-0.1294` n `18`; unknown avg `0.0368` n `384`
- 4h: commodity avg `0.6893` n `12`; crypto_alt avg `0.4887` n `228`; crypto_major avg `0.199` n `8`; equity avg `0.3282` n `66`; fx avg `-0.0396` n `6`; index avg `0.1777` n `23`; metal avg `0.0146` n `18`; unknown avg `-0.0007` n `384`
- 24h: commodity avg `-2.0574` n `12`; crypto_alt avg `2.963` n `228`; crypto_major avg `1.8422` n `8`; equity avg `1.7001` n `66`; fx avg `-0.0916` n `6`; index avg `1.1918` n `23`; metal avg `1.5465` n `18`; unknown avg `0.9117` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
