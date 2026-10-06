# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T12:37:31.522701+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1004` n `13`; crypto_alt avg `-0.0647` n `235`; crypto_major avg `-0.0562` n `8`; equity avg `-0.1132` n `150`; fx avg `-0.0038` n `6`; index avg `-0.031` n `26`; metal avg `-0.0886` n `20`; unknown avg `0.7413` n `1072`
- 1h: commodity avg `-0.0646` n `13`; crypto_alt avg `-0.175` n `235`; crypto_major avg `-0.0602` n `8`; equity avg `-0.0539` n `150`; fx avg `0.0246` n `6`; index avg `-0.0042` n `26`; metal avg `-0.0631` n `20`; unknown avg `0.408` n `1064`
- 4h: commodity avg `-0.2667` n `13`; crypto_alt avg `0.2422` n `235`; crypto_major avg `0.2704` n `8`; equity avg `0.3247` n `149`; fx avg `0.0957` n `6`; index avg `0.0781` n `26`; metal avg `-0.0324` n `20`; unknown avg `1.0482` n `1064`
- 24h: commodity avg `-0.7178` n `13`; crypto_alt avg `-0.4876` n `235`; crypto_major avg `-0.0155` n `8`; equity avg `0.7277` n `149`; fx avg `0.0909` n `6`; index avg `0.2506` n `26`; metal avg `-0.1481` n `20`; unknown avg `0.06` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1701`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
