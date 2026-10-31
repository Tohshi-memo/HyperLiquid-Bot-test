# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T22:07:27.876053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `13`; crypto_alt avg `0.2353` n `238`; crypto_major avg `0.1953` n `8`; equity avg `0.0385` n `156`; fx avg `-0.0063` n `6`; index avg `0.0078` n `27`; metal avg `0.0069` n `20`; unknown avg `-0.2443` n `1202`
- 1h: commodity avg `0.0016` n `13`; crypto_alt avg `0.2469` n `238`; crypto_major avg `0.2886` n `8`; equity avg `0.0484` n `156`; fx avg `0.0062` n `6`; index avg `0.0063` n `27`; metal avg `0.017` n `20`; unknown avg `5.2203` n `1150`
- 4h: commodity avg `0.0265` n `13`; crypto_alt avg `-0.1116` n `238`; crypto_major avg `0.0326` n `8`; equity avg `0.05` n `156`; fx avg `0.0079` n `6`; index avg `0.0027` n `27`; metal avg `0.0111` n `20`; unknown avg `1.5431` n `1120`
- 24h: commodity avg `-0.1031` n `13`; crypto_alt avg `0.3445` n `238`; crypto_major avg `0.4588` n `8`; equity avg `0.2633` n `156`; fx avg `0.0222` n `6`; index avg `-0.0447` n `27`; metal avg `0.0514` n `20`; unknown avg `1.6318` n `1059`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
