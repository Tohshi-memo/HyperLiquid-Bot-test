# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T15:37:30.768982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1018` n `12`; crypto_alt avg `-0.1399` n `231`; crypto_major avg `-0.3063` n `8`; equity avg `0.4523` n `122`; fx avg `-0.0112` n `6`; index avg `0.0803` n `25`; metal avg `-0.0074` n `20`; unknown avg `0.2876` n `793`
- 1h: commodity avg `-0.1721` n `12`; crypto_alt avg `0.2543` n `231`; crypto_major avg `-0.1786` n `8`; equity avg `0.3689` n `122`; fx avg `-0.0068` n `6`; index avg `0.0356` n `25`; metal avg `-0.0027` n `20`; unknown avg `0.374` n `793`
- 4h: commodity avg `-0.2299` n `12`; crypto_alt avg `0.6186` n `231`; crypto_major avg `0.5757` n `8`; equity avg `-0.8097` n `122`; fx avg `-0.0026` n `6`; index avg `-0.1733` n `25`; metal avg `0.1021` n `20`; unknown avg `0.658` n `793`
- 24h: commodity avg `-0.2968` n `12`; crypto_alt avg `0.2634` n `231`; crypto_major avg `1.0909` n `8`; equity avg `-2.2315` n `122`; fx avg `-0.1201` n `6`; index avg `-0.2959` n `25`; metal avg `0.3501` n `20`; unknown avg `3.5413` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
