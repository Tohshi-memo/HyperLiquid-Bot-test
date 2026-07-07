# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T12:22:30.879570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0256` n `12`; crypto_alt avg `-0.0307` n `229`; crypto_major avg `0.0396` n `8`; equity avg `-0.0756` n `91`; fx avg `-0.0284` n `6`; index avg `0.0144` n `25`; metal avg `0.0592` n `20`; unknown avg `-0.0188` n `763`
- 1h: commodity avg `-0.286` n `12`; crypto_alt avg `0.4736` n `229`; crypto_major avg `0.7921` n `8`; equity avg `0.2119` n `91`; fx avg `-0.0265` n `6`; index avg `0.11` n `25`; metal avg `0.2527` n `20`; unknown avg `0.2672` n `763`
- 4h: commodity avg `-0.2649` n `12`; crypto_alt avg `0.6445` n `229`; crypto_major avg `0.7026` n `8`; equity avg `-0.1413` n `91`; fx avg `-0.1036` n `6`; index avg `0.0193` n `25`; metal avg `0.3518` n `20`; unknown avg `-0.1073` n `757`
- 24h: commodity avg `0.1413` n `12`; crypto_alt avg `2.0175` n `229`; crypto_major avg `1.4005` n `8`; equity avg `-1.3197` n `90`; fx avg `-0.1767` n `6`; index avg `-0.3402` n `25`; metal avg `0.1467` n `20`; unknown avg `-0.218` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
