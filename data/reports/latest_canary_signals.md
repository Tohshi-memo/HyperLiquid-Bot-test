# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T02:37:26.965771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0683` n `12`; crypto_alt avg `0.2927` n `231`; crypto_major avg `0.1803` n `8`; equity avg `0.0185` n `122`; fx avg `0.0178` n `6`; index avg `0.0161` n `25`; metal avg `0.0008` n `20`; unknown avg `-0.0916` n `793`
- 1h: commodity avg `0.1082` n `12`; crypto_alt avg `0.3305` n `231`; crypto_major avg `0.5799` n `8`; equity avg `-0.4144` n `122`; fx avg `-0.0419` n `6`; index avg `-0.018` n `25`; metal avg `0.2036` n `20`; unknown avg `-0.218` n `793`
- 4h: commodity avg `-0.1345` n `12`; crypto_alt avg `-1.5737` n `231`; crypto_major avg `-0.7549` n `8`; equity avg `-1.0024` n `122`; fx avg `-0.0731` n `6`; index avg `-0.0416` n `25`; metal avg `0.1189` n `20`; unknown avg `0.6864` n `793`
- 24h: commodity avg `-0.3134` n `12`; crypto_alt avg `2.6841` n `231`; crypto_major avg `0.6366` n `8`; equity avg `-0.5157` n `122`; fx avg `-0.1906` n `6`; index avg `0.0093` n `25`; metal avg `0.199` n `20`; unknown avg `6.1085` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
