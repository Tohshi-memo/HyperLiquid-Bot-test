# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T16:07:13.961389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0168` n `12`; crypto_alt avg `0.0077` n `228`; crypto_major avg `0.0221` n `8`; equity avg `0.0186` n `65`; fx avg `-0.0068` n `5`; index avg `-0.0003` n `23`; metal avg `-0.0181` n `18`; unknown avg `-0.1859` n `376`
- 1h: commodity avg `-0.0954` n `12`; crypto_alt avg `0.0318` n `228`; crypto_major avg `0.2182` n `8`; equity avg `0.042` n `65`; fx avg `-0.0316` n `5`; index avg `0.0143` n `23`; metal avg `-0.003` n `18`; unknown avg `-0.0676` n `376`
- 4h: commodity avg `0.4218` n `12`; crypto_alt avg `-1.1189` n `228`; crypto_major avg `-0.5334` n `8`; equity avg `0.0317` n `65`; fx avg `-0.0138` n `5`; index avg `0.0473` n `23`; metal avg `-0.1087` n `18`; unknown avg `-0.5403` n `376`
- 24h: commodity avg `-0.2905` n `12`; crypto_alt avg `1.156` n `228`; crypto_major avg `1.1756` n `8`; equity avg `1.6774` n `65`; fx avg `0.0132` n `5`; index avg `0.6543` n `23`; metal avg `0.1191` n `18`; unknown avg `0.1727` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
