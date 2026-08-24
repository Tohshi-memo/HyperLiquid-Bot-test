# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T06:07:26.088148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0608` n `12`; crypto_alt avg `-0.2403` n `231`; crypto_major avg `-0.0904` n `8`; equity avg `-0.1027` n `122`; fx avg `-0.0078` n `6`; index avg `-0.0254` n `25`; metal avg `0.0534` n `20`; unknown avg `-0.0267` n `777`
- 1h: commodity avg `-0.0334` n `12`; crypto_alt avg `0.0269` n `231`; crypto_major avg `0.0173` n `8`; equity avg `-0.362` n `122`; fx avg `-0.0098` n `6`; index avg `-0.0767` n `25`; metal avg `0.0376` n `20`; unknown avg `-0.0599` n `777`
- 4h: commodity avg `0.0462` n `12`; crypto_alt avg `0.4646` n `231`; crypto_major avg `0.1162` n `8`; equity avg `-0.8366` n `122`; fx avg `-0.0181` n `6`; index avg `-0.0998` n `25`; metal avg `0.0595` n `20`; unknown avg `0.0047` n `777`
- 24h: commodity avg `-0.3146` n `12`; crypto_alt avg `4.5269` n `231`; crypto_major avg `1.9657` n `8`; equity avg `-1.183` n `122`; fx avg `-0.1944` n `6`; index avg `-0.1333` n `25`; metal avg `0.1986` n `20`; unknown avg `5.7932` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
