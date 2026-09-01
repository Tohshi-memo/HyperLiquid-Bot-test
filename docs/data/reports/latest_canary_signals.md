# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T12:52:28.603253+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `12`; crypto_alt avg `0.1179` n `232`; crypto_major avg `0.3143` n `8`; equity avg `0.0659` n `130`; fx avg `-0.0144` n `6`; index avg `0.0143` n `26`; metal avg `0.0744` n `20`; unknown avg `-0.0474` n `792`
- 1h: commodity avg `-0.0022` n `12`; crypto_alt avg `-0.6914` n `232`; crypto_major avg `-0.4484` n `8`; equity avg `-0.3816` n `130`; fx avg `-0.0081` n `6`; index avg `-0.0537` n `26`; metal avg `-0.0292` n `20`; unknown avg `-0.0301` n `790`
- 4h: commodity avg `-0.1282` n `12`; crypto_alt avg `0.2479` n `232`; crypto_major avg `0.2395` n `8`; equity avg `-0.6` n `130`; fx avg `0.0134` n `6`; index avg `-0.1033` n `26`; metal avg `0.0273` n `20`; unknown avg `-0.5543` n `790`
- 24h: commodity avg `0.3607` n `12`; crypto_alt avg `1.1375` n `232`; crypto_major avg `0.4757` n `8`; equity avg `-0.7066` n `130`; fx avg `0.0727` n `6`; index avg `-0.2675` n `26`; metal avg `-0.5994` n `20`; unknown avg `-0.0708` n `750`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0402`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0309`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0306`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0283`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.028`, n `668`, weak_sample_signal
