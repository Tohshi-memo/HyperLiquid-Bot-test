# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T13:37:29.134677+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.162` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `-0.881` n `231`; crypto_major avg `-0.7497` n `8`; equity avg `-0.9458` n `122`; fx avg `0.0011` n `6`; index avg `-0.112` n `25`; metal avg `0.0595` n `20`; unknown avg `1.6023` n `793`
- 1h: commodity avg `0.0184` n `12`; crypto_alt avg `-0.4069` n `231`; crypto_major avg `-0.2925` n `8`; equity avg `-0.9824` n `122`; fx avg `0.0293` n `6`; index avg `-0.1154` n `25`; metal avg `0.1523` n `20`; unknown avg `0.4697` n `793`
- 4h: commodity avg `0.2288` n `12`; crypto_alt avg `0.3968` n `231`; crypto_major avg `0.9772` n `8`; equity avg `-1.1848` n `122`; fx avg `0.0467` n `6`; index avg `-0.1535` n `25`; metal avg `0.297` n `20`; unknown avg `0.9405` n `793`
- 24h: commodity avg `0.0413` n `12`; crypto_alt avg `-0.2368` n `231`; crypto_major avg `0.1012` n `8`; equity avg `-2.598` n `122`; fx avg `-0.1145` n `6`; index avg `-0.2831` n `25`; metal avg `0.3452` n `20`; unknown avg `3.8493` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
