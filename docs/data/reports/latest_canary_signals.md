# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T18:07:28.614118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5123` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0031` n `12`; crypto_alt avg `0.526` n `231`; crypto_major avg `0.3967` n `8`; equity avg `0.2862` n `122`; fx avg `0.0019` n `6`; index avg `0.0571` n `25`; metal avg `0.0219` n `20`; unknown avg `-0.0126` n `794`
- 1h: commodity avg `0.0244` n `12`; crypto_alt avg `-0.4361` n `231`; crypto_major avg `-0.5826` n `8`; equity avg `-0.093` n `122`; fx avg `-0.0026` n `6`; index avg `-0.0073` n `25`; metal avg `-0.1123` n `20`; unknown avg `-0.1653` n `794`
- 4h: commodity avg `-0.2139` n `12`; crypto_alt avg `-0.0893` n `231`; crypto_major avg `-0.6005` n `8`; equity avg `0.9118` n `122`; fx avg `-0.0245` n `6`; index avg `0.1238` n `25`; metal avg `-0.2138` n `20`; unknown avg `-0.1371` n `793`
- 24h: commodity avg `-0.2573` n `12`; crypto_alt avg `-1.0122` n `231`; crypto_major avg `-0.3024` n `8`; equity avg `-2.3688` n `122`; fx avg `-0.1481` n `6`; index avg `-0.3047` n `25`; metal avg `0.0479` n `20`; unknown avg `3.4028` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
