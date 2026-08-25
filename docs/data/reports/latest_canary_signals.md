# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T00:22:43.012387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0187` n `12`; crypto_alt avg `-0.1347` n `231`; crypto_major avg `0.0137` n `8`; equity avg `-0.0986` n `122`; fx avg `0.0111` n `6`; index avg `-0.0292` n `25`; metal avg `-0.0531` n `20`; unknown avg `-0.0354` n `794`
- 1h: commodity avg `-0.009` n `12`; crypto_alt avg `0.3361` n `231`; crypto_major avg `0.494` n `8`; equity avg `-0.3428` n `122`; fx avg `-0.0022` n `6`; index avg `-0.1124` n `25`; metal avg `0.0003` n `20`; unknown avg `-0.0323` n `794`
- 4h: commodity avg `0.036` n `12`; crypto_alt avg `0.4477` n `231`; crypto_major avg `1.0828` n `8`; equity avg `-0.2995` n `122`; fx avg `-0.0033` n `6`; index avg `-0.1078` n `25`; metal avg `0.1523` n `20`; unknown avg `-0.2845` n `794`
- 24h: commodity avg `-0.068` n `12`; crypto_alt avg `-0.5162` n `231`; crypto_major avg `0.1837` n `8`; equity avg `-2.7709` n `122`; fx avg `-0.0377` n `6`; index avg `-0.3917` n `25`; metal avg `0.2394` n `20`; unknown avg `0.8242` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
