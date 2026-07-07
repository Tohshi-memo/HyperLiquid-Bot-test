# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T08:37:30.706735+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `12`; crypto_alt avg `-0.1402` n `229`; crypto_major avg `-0.1752` n `8`; equity avg `-0.0555` n `91`; fx avg `0.0168` n `6`; index avg `0.0074` n `25`; metal avg `-0.0376` n `20`; unknown avg `2.7822` n `763`
- 1h: commodity avg `-0.0113` n `12`; crypto_alt avg `-0.0811` n `229`; crypto_major avg `-0.1236` n `8`; equity avg `-0.0558` n `91`; fx avg `-0.0241` n `6`; index avg `0.0001` n `25`; metal avg `0.0468` n `20`; unknown avg `2.6936` n `763`
- 4h: commodity avg `0.2388` n `12`; crypto_alt avg `0.0787` n `229`; crypto_major avg `0.1888` n `8`; equity avg `0.4839` n `91`; fx avg `-0.0156` n `6`; index avg `0.0995` n `25`; metal avg `0.0799` n `20`; unknown avg `3.8994` n `745`
- 24h: commodity avg `0.4465` n `12`; crypto_alt avg `0.5546` n `229`; crypto_major avg `-0.2073` n `8`; equity avg `-1.3173` n `90`; fx avg `-0.0651` n `6`; index avg `-0.3223` n `25`; metal avg `-0.282` n `20`; unknown avg `-0.4758` n `743`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
