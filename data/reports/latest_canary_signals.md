# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T09:52:26.802442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0364` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0412` n `12`; crypto_alt avg `0.1376` n `228`; crypto_major avg `0.1013` n `8`; equity avg `0.0807` n `74`; fx avg `0.0114` n `6`; index avg `0.0458` n `23`; metal avg `0.1194` n `18`; unknown avg `0.2931` n `547`
- 1h: commodity avg `-0.1821` n `12`; crypto_alt avg `-0.6941` n `228`; crypto_major avg `-0.638` n `8`; equity avg `0.0608` n `74`; fx avg `0.0414` n `6`; index avg `0.0677` n `23`; metal avg `0.0951` n `18`; unknown avg `-0.0472` n `547`
- 4h: commodity avg `-0.2378` n `12`; crypto_alt avg `-0.7216` n `228`; crypto_major avg `-0.8745` n `8`; equity avg `0.0151` n `74`; fx avg `0.1831` n `6`; index avg `0.1619` n `23`; metal avg `0.0977` n `18`; unknown avg `0.0251` n `503`
- 24h: commodity avg `-1.4025` n `12`; crypto_alt avg `-0.659` n `228`; crypto_major avg `0.0686` n `8`; equity avg `2.3169` n `74`; fx avg `0.1017` n `6`; index avg `1.1683` n `23`; metal avg `0.9182` n `18`; unknown avg `-2.8866` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
