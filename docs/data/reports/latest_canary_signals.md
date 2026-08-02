# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T05:22:30.083410+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0287` n `12`; crypto_alt avg `0.0196` n `230`; crypto_major avg `0.0144` n `8`; equity avg `-0.0066` n `102`; fx avg `-0.0075` n `6`; index avg `0.0046` n `25`; metal avg `-0.0027` n `20`; unknown avg `0.3378` n `782`
- 1h: commodity avg `0.0738` n `12`; crypto_alt avg `0.1407` n `230`; crypto_major avg `0.0224` n `8`; equity avg `-0.0177` n `102`; fx avg `-0.0013` n `6`; index avg `-0.0014` n `25`; metal avg `-0.0227` n `20`; unknown avg `0.3712` n `782`
- 4h: commodity avg `-0.8349` n `12`; crypto_alt avg `0.7197` n `230`; crypto_major avg `0.9743` n `8`; equity avg `0.7135` n `102`; fx avg `-0.0614` n `6`; index avg `0.2107` n `25`; metal avg `0.1451` n `20`; unknown avg `1.2249` n `782`
- 24h: commodity avg `-1.0526` n `12`; crypto_alt avg `0.1262` n `230`; crypto_major avg `0.4344` n `8`; equity avg `0.8194` n `102`; fx avg `-0.1258` n `6`; index avg `0.26` n `25`; metal avg `0.2518` n `20`; unknown avg `0.4033` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
