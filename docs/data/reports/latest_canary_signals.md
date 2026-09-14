# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T19:22:27.697573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5113` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0568` n `12`; crypto_alt avg `0.0062` n `233`; crypto_major avg `0.1376` n `8`; equity avg `-0.1` n `136`; fx avg `0.0072` n `6`; index avg `-0.0107` n `27`; metal avg `-0.0498` n `20`; unknown avg `0.4826` n `908`
- 1h: commodity avg `-0.0973` n `12`; crypto_alt avg `-0.0591` n `233`; crypto_major avg `0.1364` n `8`; equity avg `-0.2724` n `136`; fx avg `-0.0174` n `6`; index avg `-0.0326` n `27`; metal avg `-0.0756` n `20`; unknown avg `0.6903` n `906`
- 4h: commodity avg `-0.3657` n `12`; crypto_alt avg `1.2924` n `233`; crypto_major avg `1.6322` n `8`; equity avg `0.4925` n `136`; fx avg `-0.0` n `6`; index avg `0.1475` n `27`; metal avg `0.1209` n `20`; unknown avg `1.0929` n `878`
- 24h: commodity avg `0.1185` n `12`; crypto_alt avg `0.5646` n `233`; crypto_major avg `2.6053` n `8`; equity avg `-0.4594` n `136`; fx avg `0.0478` n `6`; index avg `-0.1456` n `27`; metal avg `-0.3628` n `20`; unknown avg `3.347` n `696`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
