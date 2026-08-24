# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T04:37:27.662151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0173` n `12`; crypto_alt avg `-0.0336` n `231`; crypto_major avg `-0.0692` n `8`; equity avg `-0.0373` n `122`; fx avg `-0.0058` n `6`; index avg `-0.0063` n `25`; metal avg `-0.01` n `20`; unknown avg `-0.0477` n `793`
- 1h: commodity avg `-0.0254` n `12`; crypto_alt avg `0.6722` n `231`; crypto_major avg `0.4049` n `8`; equity avg `0.0748` n `122`; fx avg `0.0023` n `6`; index avg `0.0029` n `25`; metal avg `-0.1035` n `20`; unknown avg `-0.2476` n `793`
- 4h: commodity avg `-0.037` n `12`; crypto_alt avg `-0.7926` n `231`; crypto_major avg `-0.709` n `8`; equity avg `-1.1486` n `122`; fx avg `-0.0203` n `6`; index avg `-0.1135` n `25`; metal avg `0.096` n `20`; unknown avg `0.3042` n `793`
- 24h: commodity avg `-0.3031` n `12`; crypto_alt avg `4.2249` n `231`; crypto_major avg `1.3175` n `8`; equity avg `-1.0669` n `122`; fx avg `-0.193` n `6`; index avg `-0.1057` n `25`; metal avg `0.0996` n `20`; unknown avg `6.0397` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
