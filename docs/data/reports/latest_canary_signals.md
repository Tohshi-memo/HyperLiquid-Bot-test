# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T00:37:24.004518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0261` n `12`; crypto_alt avg `0.1361` n `231`; crypto_major avg `-0.0052` n `8`; equity avg `-0.104` n `122`; fx avg `-0.0109` n `6`; index avg `-0.0016` n `25`; metal avg `-0.1044` n `20`; unknown avg `0.0103` n `793`
- 1h: commodity avg `-0.0784` n `12`; crypto_alt avg `-0.746` n `231`; crypto_major avg `-0.5916` n `8`; equity avg `-0.6601` n `122`; fx avg `-0.0343` n `6`; index avg `-0.1057` n `25`; metal avg `-0.0882` n `20`; unknown avg `0.2674` n `793`
- 4h: commodity avg `-0.1948` n `12`; crypto_alt avg `-0.6312` n `231`; crypto_major avg `0.1143` n `8`; equity avg `-0.5328` n `122`; fx avg `-0.0475` n `6`; index avg `-0.0817` n `25`; metal avg `-0.1082` n `20`; unknown avg `0.6144` n `793`
- 24h: commodity avg `-0.308` n `12`; crypto_alt avg `2.0088` n `231`; crypto_major avg `0.2402` n `8`; equity avg `0.0557` n `122`; fx avg `-0.1615` n `6`; index avg `0.0252` n `25`; metal avg `0.0036` n `20`; unknown avg `5.7137` n `776`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
