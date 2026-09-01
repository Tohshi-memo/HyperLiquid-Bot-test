# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T01:37:23.592836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0223` n `12`; crypto_alt avg `-0.0056` n `232`; crypto_major avg `-0.0983` n `8`; equity avg `-0.0709` n `130`; fx avg `-0.0021` n `6`; index avg `-0.0189` n `26`; metal avg `-0.0135` n `20`; unknown avg `-0.0455` n `792`
- 1h: commodity avg `0.0212` n `12`; crypto_alt avg `-0.0467` n `232`; crypto_major avg `-0.2948` n `8`; equity avg `0.0416` n `130`; fx avg `0.0102` n `6`; index avg `0.0314` n `26`; metal avg `-0.0253` n `20`; unknown avg `0.4146` n `790`
- 4h: commodity avg `0.0847` n `12`; crypto_alt avg `0.3582` n `232`; crypto_major avg `-0.5528` n `8`; equity avg `0.0809` n `130`; fx avg `0.0339` n `6`; index avg `0.0547` n `26`; metal avg `0.0581` n `20`; unknown avg `0.0884` n `790`
- 24h: commodity avg `0.4361` n `12`; crypto_alt avg `2.0859` n `231`; crypto_major avg `1.5725` n `8`; equity avg `1.4126` n `130`; fx avg `-0.0134` n `6`; index avg `0.2085` n `26`; metal avg `-0.0091` n `20`; unknown avg `0.2901` n `739`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
