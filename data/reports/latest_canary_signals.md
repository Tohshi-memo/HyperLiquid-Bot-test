# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T01:52:30.989172+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5543` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5452` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0145` n `12`; crypto_alt avg `-0.1001` n `231`; crypto_major avg `-0.0858` n `8`; equity avg `-0.079` n `122`; fx avg `-0.0023` n `6`; index avg `0.0089` n `25`; metal avg `0.0409` n `20`; unknown avg `-0.0697` n `793`
- 1h: commodity avg `-0.095` n `12`; crypto_alt avg `-0.9279` n `231`; crypto_major avg `-0.8777` n `8`; equity avg `-0.3891` n `122`; fx avg `0.0298` n `6`; index avg `-0.0102` n `25`; metal avg `-0.0262` n `20`; unknown avg `0.8766` n `793`
- 4h: commodity avg `-0.2683` n `12`; crypto_alt avg `-2.3484` n `231`; crypto_major avg `-1.6035` n `8`; equity avg `-0.7613` n `122`; fx avg `-0.0146` n `6`; index avg `-0.0583` n `25`; metal avg `-0.0492` n `20`; unknown avg `0.8736` n `793`
- 24h: commodity avg `-0.3927` n `12`; crypto_alt avg `1.8049` n `231`; crypto_major avg `-0.4047` n `8`; equity avg `-0.1821` n `122`; fx avg `-0.1408` n `6`; index avg `0.0425` n `25`; metal avg `0.0341` n `20`; unknown avg `6.1255` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
