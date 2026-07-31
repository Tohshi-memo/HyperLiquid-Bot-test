# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T07:22:25.896207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `-0.0978` n `230`; crypto_major avg `-0.2384` n `8`; equity avg `0.0671` n `102`; fx avg `0.015` n `6`; index avg `0.0285` n `25`; metal avg `-0.0081` n `20`; unknown avg `-0.0447` n `779`
- 1h: commodity avg `0.0533` n `12`; crypto_alt avg `-0.3372` n `230`; crypto_major avg `-0.5684` n `8`; equity avg `-0.743` n `102`; fx avg `-0.0128` n `6`; index avg `-0.1316` n `25`; metal avg `-0.1208` n `20`; unknown avg `-0.061` n `779`
- 4h: commodity avg `0.0383` n `12`; crypto_alt avg `-0.286` n `230`; crypto_major avg `-0.3738` n `8`; equity avg `0.0172` n `102`; fx avg `-0.1036` n `6`; index avg `0.0398` n `25`; metal avg `0.0209` n `20`; unknown avg `-0.0664` n `747`
- 24h: commodity avg `-0.4033` n `12`; crypto_alt avg `-0.35` n `230`; crypto_major avg `0.3902` n `8`; equity avg `8.5438` n `102`; fx avg `-0.136` n `6`; index avg `1.3088` n `25`; metal avg `0.5272` n `20`; unknown avg `0.003` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
