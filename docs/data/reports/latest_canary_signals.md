# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T07:07:33.226545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.036` n `12`; crypto_alt avg `-0.2747` n `230`; crypto_major avg `-0.2487` n `8`; equity avg `-0.0302` n `102`; fx avg `0.0379` n `6`; index avg `0.0001` n `25`; metal avg `-0.026` n `20`; unknown avg `-0.0386` n `779`
- 1h: commodity avg `0.107` n `12`; crypto_alt avg `-0.22` n `230`; crypto_major avg `-0.2512` n `8`; equity avg `-0.8801` n `102`; fx avg `-0.0441` n `6`; index avg `-0.1348` n `25`; metal avg `-0.0736` n `20`; unknown avg `0.0286` n `779`
- 4h: commodity avg `0.053` n `12`; crypto_alt avg `0.0811` n `230`; crypto_major avg `0.0791` n `8`; equity avg `0.1629` n `102`; fx avg `-0.0953` n `6`; index avg `0.0583` n `25`; metal avg `0.0107` n `20`; unknown avg `-0.0093` n `747`
- 24h: commodity avg `-0.3727` n `12`; crypto_alt avg `-0.2197` n `230`; crypto_major avg `0.6815` n `8`; equity avg `8.2195` n `102`; fx avg `-0.148` n `6`; index avg `1.2047` n `25`; metal avg `0.5295` n `20`; unknown avg `0.0295` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
