# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T16:07:53.256090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0127` n `12`; crypto_alt avg `0.0404` n `230`; crypto_major avg `0.1068` n `8`; equity avg `0.0041` n `108`; fx avg `0.0069` n `6`; index avg `-0.0157` n `25`; metal avg `-0.0505` n `20`; unknown avg `0.007` n `782`
- 1h: commodity avg `0.1098` n `12`; crypto_alt avg `-0.0827` n `230`; crypto_major avg `-0.034` n `8`; equity avg `-0.1284` n `108`; fx avg `0.0195` n `6`; index avg `-0.08` n `25`; metal avg `-0.1187` n `20`; unknown avg `-0.0147` n `782`
- 4h: commodity avg `-0.1398` n `12`; crypto_alt avg `0.0474` n `230`; crypto_major avg `0.4003` n `8`; equity avg `-0.0835` n `108`; fx avg `-0.0232` n `6`; index avg `-0.0782` n `25`; metal avg `-0.0716` n `20`; unknown avg `-0.0095` n `782`
- 24h: commodity avg `-0.0297` n `12`; crypto_alt avg `0.6693` n `230`; crypto_major avg `0.65` n `8`; equity avg `0.0309` n `108`; fx avg `0.0136` n `6`; index avg `0.0622` n `25`; metal avg `0.5974` n `20`; unknown avg `0.7534` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
