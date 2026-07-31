# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T21:37:36.441092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1788` n `12`; crypto_alt avg `-0.1478` n `230`; crypto_major avg `-0.1065` n `8`; equity avg `-0.0318` n `102`; fx avg `0.0125` n `6`; index avg `-0.039` n `25`; metal avg `0.0002` n `20`; unknown avg `-0.2501` n `781`
- 1h: commodity avg `0.6931` n `12`; crypto_alt avg `-0.2067` n `230`; crypto_major avg `-0.1313` n `8`; equity avg `-0.1971` n `102`; fx avg `-0.0118` n `6`; index avg `-0.0835` n `25`; metal avg `-0.0619` n `20`; unknown avg `-0.2592` n `780`
- 4h: commodity avg `0.7769` n `12`; crypto_alt avg `-0.5957` n `230`; crypto_major avg `-0.5687` n `8`; equity avg `-1.085` n `102`; fx avg `-0.0037` n `6`; index avg `-0.1533` n `25`; metal avg `-0.0501` n `20`; unknown avg `7.0003` n `780`
- 24h: commodity avg `0.8846` n `12`; crypto_alt avg `-0.7077` n `230`; crypto_major avg `-2.1331` n `8`; equity avg `-1.2982` n `102`; fx avg `0.1251` n `6`; index avg `0.058` n `25`; metal avg `-0.4308` n `20`; unknown avg `0.161` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
