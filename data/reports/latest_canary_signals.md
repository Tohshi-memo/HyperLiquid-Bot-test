# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T16:22:38.237905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.049` n `12`; crypto_alt avg `0.1328` n `231`; crypto_major avg `0.1632` n `8`; equity avg `0.2229` n `122`; fx avg `-0.0044` n `6`; index avg `0.0272` n `25`; metal avg `-0.0011` n `20`; unknown avg `2.0132` n `793`
- 1h: commodity avg `-0.0306` n `12`; crypto_alt avg `-0.3265` n `231`; crypto_major avg `-0.3545` n `8`; equity avg `0.7152` n `122`; fx avg `-0.0333` n `6`; index avg `0.128` n `25`; metal avg `-0.1317` n `20`; unknown avg `1.1303` n `793`
- 4h: commodity avg `-0.2292` n `12`; crypto_alt avg `0.8379` n `231`; crypto_major avg `0.7478` n `8`; equity avg `-0.3577` n `122`; fx avg `-0.0026` n `6`; index avg `-0.0868` n `25`; metal avg `0.0473` n `20`; unknown avg `0.654` n `793`
- 24h: commodity avg `-0.1972` n `12`; crypto_alt avg `0.349` n `231`; crypto_major avg `1.2485` n `8`; equity avg `-1.9719` n `122`; fx avg `-0.1339` n `6`; index avg `-0.2482` n `25`; metal avg `0.2012` n `20`; unknown avg `3.8153` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
