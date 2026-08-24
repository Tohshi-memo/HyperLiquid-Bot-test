# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T08:07:25.906007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0333` n `12`; crypto_alt avg `0.0716` n `231`; crypto_major avg `-0.1951` n `8`; equity avg `0.0411` n `122`; fx avg `0.0095` n `6`; index avg `-0.0021` n `25`; metal avg `0.0409` n `20`; unknown avg `-0.0084` n `793`
- 1h: commodity avg `0.1736` n `12`; crypto_alt avg `0.062` n `231`; crypto_major avg `-0.4613` n `8`; equity avg `-0.0583` n `122`; fx avg `0.0004` n `6`; index avg `-0.0072` n `25`; metal avg `-0.0452` n `20`; unknown avg `-0.0097` n `793`
- 4h: commodity avg `0.1148` n `12`; crypto_alt avg `0.3002` n `231`; crypto_major avg `0.0743` n `8`; equity avg `-0.2409` n `122`; fx avg `0.0324` n `6`; index avg `-0.0491` n `25`; metal avg `0.0637` n `20`; unknown avg `-0.0178` n `777`
- 24h: commodity avg `-0.2002` n `12`; crypto_alt avg `2.7262` n `231`; crypto_major avg `0.9019` n `8`; equity avg `-1.3301` n `122`; fx avg `-0.1218` n `6`; index avg `-0.1361` n `25`; metal avg `0.1657` n `20`; unknown avg `5.1759` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
