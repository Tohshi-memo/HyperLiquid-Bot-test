# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T03:07:27.863908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.054` n `12`; crypto_alt avg `-0.1908` n `231`; crypto_major avg `-0.1585` n `8`; equity avg `-0.1024` n `122`; fx avg `0.0169` n `6`; index avg `-0.0081` n `25`; metal avg `0.0212` n `20`; unknown avg `0.0647` n `793`
- 1h: commodity avg `0.1036` n `12`; crypto_alt avg `0.4227` n `231`; crypto_major avg `0.3671` n `8`; equity avg `-0.2045` n `122`; fx avg `0.0095` n `6`; index avg `0.0224` n `25`; metal avg `-0.0144` n `20`; unknown avg `-0.1065` n `793`
- 4h: commodity avg `-0.0595` n `12`; crypto_alt avg `-1.8846` n `231`; crypto_major avg `-1.1054` n `8`; equity avg `-1.3531` n `122`; fx avg `-0.0445` n `6`; index avg `-0.1065` n `25`; metal avg `0.0768` n `20`; unknown avg `0.7626` n `793`
- 24h: commodity avg `-0.2742` n `12`; crypto_alt avg `2.7817` n `231`; crypto_major avg `0.4643` n `8`; equity avg `-0.8183` n `122`; fx avg `-0.1862` n `6`; index avg `-0.0336` n `25`; metal avg `0.0876` n `20`; unknown avg `5.9505` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
