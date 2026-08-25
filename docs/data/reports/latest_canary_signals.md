# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T00:25:12.844236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.506` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0189` n `12`; crypto_alt avg `-0.0666` n `231`; crypto_major avg `0.1582` n `8`; equity avg `-0.0753` n `122`; fx avg `0.0111` n `6`; index avg `-0.0235` n `25`; metal avg `-0.0769` n `20`; unknown avg `-0.0813` n `794`
- 1h: commodity avg `-0.0091` n `12`; crypto_alt avg `0.4045` n `231`; crypto_major avg `0.6397` n `8`; equity avg `-0.3196` n `122`; fx avg `-0.0022` n `6`; index avg `-0.1067` n `25`; metal avg `-0.0235` n `20`; unknown avg `-0.053` n `794`
- 4h: commodity avg `0.0358` n `12`; crypto_alt avg `0.5169` n `231`; crypto_major avg `1.2298` n `8`; equity avg `-0.2762` n `122`; fx avg `-0.0033` n `6`; index avg `-0.1022` n `25`; metal avg `0.1284` n `20`; unknown avg `-0.269` n `794`
- 24h: commodity avg `-0.068` n `12`; crypto_alt avg `-0.4472` n `231`; crypto_major avg `0.3274` n `8`; equity avg `-2.7495` n `122`; fx avg `-0.0377` n `6`; index avg `-0.3862` n `25`; metal avg `0.2154` n `20`; unknown avg `0.8251` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
