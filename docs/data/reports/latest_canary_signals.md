# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T16:37:26.865816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `12`; crypto_alt avg `-0.1152` n `229`; crypto_major avg `-0.1848` n `8`; equity avg `0.0236` n `92`; fx avg `0.0076` n `6`; index avg `-0.0201` n `25`; metal avg `0.0344` n `20`; unknown avg `-0.0511` n `765`
- 1h: commodity avg `0.1301` n `12`; crypto_alt avg `-0.0762` n `229`; crypto_major avg `-0.1465` n `8`; equity avg `0.2261` n `92`; fx avg `-0.0048` n `6`; index avg `-0.001` n `25`; metal avg `0.0394` n `20`; unknown avg `-0.1364` n `765`
- 4h: commodity avg `-0.3432` n `12`; crypto_alt avg `-0.4324` n `229`; crypto_major avg `-0.799` n `8`; equity avg `-0.5045` n `92`; fx avg `-0.0825` n `6`; index avg `0.0719` n `25`; metal avg `0.1538` n `20`; unknown avg `-0.1267` n `765`
- 24h: commodity avg `-0.4187` n `12`; crypto_alt avg `0.9061` n `229`; crypto_major avg `1.0149` n `8`; equity avg `-0.6181` n `92`; fx avg `-0.1563` n `6`; index avg `0.0584` n `25`; metal avg `-0.1739` n `20`; unknown avg `-0.2271` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
