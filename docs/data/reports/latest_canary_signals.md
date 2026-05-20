# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T22:37:17.081307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3515` n `12`; crypto_alt avg `0.0724` n `228`; crypto_major avg `0.2964` n `8`; equity avg `0.1212` n `66`; fx avg `0.0045` n `6`; index avg `0.0404` n `23`; metal avg `0.1327` n `18`; unknown avg `-0.0247` n `384`
- 1h: commodity avg `0.284` n `12`; crypto_alt avg `-0.4104` n `228`; crypto_major avg `0.0563` n `8`; equity avg `-0.3245` n `66`; fx avg `0.01` n `6`; index avg `-0.1944` n `23`; metal avg `-0.1383` n `18`; unknown avg `-0.1353` n `384`
- 4h: commodity avg `0.5238` n `12`; crypto_alt avg `-0.226` n `228`; crypto_major avg `0.2998` n `8`; equity avg `-0.3794` n `66`; fx avg `-0.0525` n `6`; index avg `-0.1095` n `23`; metal avg `-0.3512` n `18`; unknown avg `-0.2661` n `384`
- 24h: commodity avg `-2.0952` n `12`; crypto_alt avg `2.7769` n `228`; crypto_major avg `2.3863` n `8`; equity avg `1.3932` n `66`; fx avg `-0.0692` n `6`; index avg `0.9668` n `23`; metal avg `1.2878` n `18`; unknown avg `1.0023` n `373`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0509`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
