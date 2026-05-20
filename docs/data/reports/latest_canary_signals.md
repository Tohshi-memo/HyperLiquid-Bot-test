# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T22:42:09.107756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.325` n `12`; crypto_alt avg `0.1462` n `228`; crypto_major avg `0.3184` n `8`; equity avg `0.1394` n `66`; fx avg `0.0025` n `6`; index avg `0.0536` n `23`; metal avg `0.1519` n `18`; unknown avg `-0.0387` n `384`
- 1h: commodity avg `0.2574` n `12`; crypto_alt avg `-0.3375` n `228`; crypto_major avg `0.0776` n `8`; equity avg `-0.3075` n `66`; fx avg `0.0081` n `6`; index avg `-0.1813` n `23`; metal avg `-0.1191` n `18`; unknown avg `-0.1622` n `384`
- 4h: commodity avg `0.4971` n `12`; crypto_alt avg `-0.1523` n `228`; crypto_major avg `0.3203` n `8`; equity avg `-0.3626` n `66`; fx avg `-0.0544` n `6`; index avg `-0.0964` n `23`; metal avg `-0.3322` n `18`; unknown avg `-0.2789` n `384`
- 24h: commodity avg `-2.1188` n `12`; crypto_alt avg `2.8539` n `228`; crypto_major avg `2.4049` n `8`; equity avg `1.4098` n `66`; fx avg `-0.0712` n `6`; index avg `0.9802` n `23`; metal avg `1.3074` n `18`; unknown avg `1.0095` n `373`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0459`, n `668`, weak_sample_signal
