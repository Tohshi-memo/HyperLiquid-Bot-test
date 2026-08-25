# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T09:52:38.791549+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.3175` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.8553` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7287` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0205` n `12`; crypto_alt avg `-0.5276` n `231`; crypto_major avg `-0.646` n `8`; equity avg `0.1339` n `122`; fx avg `-0.006` n `6`; index avg `0.0338` n `25`; metal avg `0.0723` n `20`; unknown avg `-0.0846` n `794`
- 1h: commodity avg `-0.2163` n `12`; crypto_alt avg `-0.2417` n `231`; crypto_major avg `-0.3532` n `8`; equity avg `0.4637` n `122`; fx avg `-0.0162` n `6`; index avg `0.1054` n `25`; metal avg `0.1351` n `20`; unknown avg `-0.0611` n `794`
- 4h: commodity avg `-0.4591` n `12`; crypto_alt avg `-1.6678` n `231`; crypto_major avg `-1.6929` n `8`; equity avg `0.6246` n `122`; fx avg `0.0195` n `6`; index avg `0.1624` n `25`; metal avg `0.0358` n `20`; unknown avg `-0.3322` n `778`
- 24h: commodity avg `-0.7081` n `12`; crypto_alt avg `0.4164` n `231`; crypto_major avg `1.3498` n `8`; equity avg `0.6667` n `122`; fx avg `0.0478` n `6`; index avg `0.1457` n `25`; metal avg `-0.1576` n `20`; unknown avg `-0.1485` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
