# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T18:22:24.156372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0804` n `12`; crypto_alt avg `0.1807` n `231`; crypto_major avg `-0.0106` n `8`; equity avg `-0.0171` n `122`; fx avg `-0.0024` n `6`; index avg `-0.0138` n `25`; metal avg `-0.0217` n `20`; unknown avg `0.0556` n `797`
- 1h: commodity avg `-0.2101` n `12`; crypto_alt avg `0.1379` n `231`; crypto_major avg `0.2891` n `8`; equity avg `0.1019` n `122`; fx avg `0.0024` n `6`; index avg `-0.0059` n `25`; metal avg `0.0126` n `20`; unknown avg `0.2102` n `797`
- 4h: commodity avg `0.0298` n `12`; crypto_alt avg `-0.5703` n `231`; crypto_major avg `-0.2782` n `8`; equity avg `0.2502` n `122`; fx avg `-0.0004` n `6`; index avg `0.0225` n `25`; metal avg `-0.2177` n `20`; unknown avg `-0.0174` n `797`
- 24h: commodity avg `0.1421` n `12`; crypto_alt avg `-2.0302` n `231`; crypto_major avg `-2.0168` n `8`; equity avg `-0.1425` n `122`; fx avg `-0.0514` n `6`; index avg `0.0387` n `25`; metal avg `-0.3096` n `20`; unknown avg `0.5183` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
