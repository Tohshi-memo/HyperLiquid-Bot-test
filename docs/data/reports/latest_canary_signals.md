# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T01:22:25.582077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0625` n `12`; crypto_alt avg `0.0817` n `230`; crypto_major avg `0.1543` n `8`; equity avg `-0.1642` n `92`; fx avg `-0.0328` n `6`; index avg `-0.0331` n `25`; metal avg `0.0241` n `20`; unknown avg `-0.0747` n `766`
- 1h: commodity avg `-0.2475` n `12`; crypto_alt avg `0.3671` n `230`; crypto_major avg `0.2788` n `8`; equity avg `0.4399` n `92`; fx avg `-0.0563` n `6`; index avg `0.1405` n `25`; metal avg `0.0454` n `20`; unknown avg `-0.0528` n `766`
- 4h: commodity avg `0.1831` n `12`; crypto_alt avg `0.7501` n `230`; crypto_major avg `0.8365` n `8`; equity avg `0.3489` n `92`; fx avg `-0.0766` n `6`; index avg `0.0631` n `25`; metal avg `-0.0688` n `20`; unknown avg `0.3206` n `766`
- 24h: commodity avg `0.8889` n `12`; crypto_alt avg `-1.3181` n `230`; crypto_major avg `-1.9273` n `8`; equity avg `-1.9145` n `92`; fx avg `-0.1604` n `6`; index avg `-0.3372` n `25`; metal avg `-0.3395` n `20`; unknown avg `-0.3304` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
