# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T02:07:24.923066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.0635` n `231`; crypto_major avg `0.0018` n `8`; equity avg `-0.0192` n `126`; fx avg `0.0099` n `6`; index avg `0.0137` n `25`; metal avg `0.0225` n `20`; unknown avg `0.0328` n `793`
- 1h: commodity avg `-0.0811` n `12`; crypto_alt avg `0.331` n `231`; crypto_major avg `0.591` n `8`; equity avg `0.1543` n `126`; fx avg `0.015` n `6`; index avg `0.0633` n `25`; metal avg `0.1031` n `20`; unknown avg `0.4676` n `793`
- 4h: commodity avg `0.016` n `12`; crypto_alt avg `0.5508` n `231`; crypto_major avg `0.6753` n `8`; equity avg `-0.2224` n `126`; fx avg `-0.064` n `6`; index avg `-0.0749` n `25`; metal avg `0.2362` n `20`; unknown avg `-0.0463` n `793`
- 24h: commodity avg `0.432` n `12`; crypto_alt avg `1.0472` n `231`; crypto_major avg `1.2364` n `8`; equity avg `1.758` n `126`; fx avg `-0.0886` n `6`; index avg `0.3175` n `25`; metal avg `-0.2111` n `20`; unknown avg `0.9709` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
