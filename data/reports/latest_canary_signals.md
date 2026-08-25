# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T11:52:29.003127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0605` n `12`; crypto_alt avg `-0.3237` n `231`; crypto_major avg `-0.3459` n `8`; equity avg `0.0678` n `122`; fx avg `-0.0125` n `6`; index avg `0.0154` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.0798` n `795`
- 1h: commodity avg `-0.0805` n `12`; crypto_alt avg `-0.4077` n `231`; crypto_major avg `-0.5068` n `8`; equity avg `-0.0934` n `122`; fx avg `-0.0084` n `6`; index avg `0.0021` n `25`; metal avg `0.0217` n `20`; unknown avg `-0.0334` n `795`
- 4h: commodity avg `-0.4675` n `12`; crypto_alt avg `-0.3442` n `231`; crypto_major avg `-0.7895` n `8`; equity avg `0.5504` n `122`; fx avg `-0.0409` n `6`; index avg `0.1239` n `25`; metal avg `0.0218` n `20`; unknown avg `-0.0695` n `794`
- 24h: commodity avg `-0.8395` n `12`; crypto_alt avg `-0.6151` n `231`; crypto_major avg `0.1232` n `8`; equity avg `0.5688` n `122`; fx avg `-0.0023` n `6`; index avg `0.1101` n `25`; metal avg `-0.1846` n `20`; unknown avg `-0.2123` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
