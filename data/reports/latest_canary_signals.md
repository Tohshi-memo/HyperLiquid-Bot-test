# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T07:52:28.804308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.5` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `-0.0968` n `231`; crypto_major avg `-0.0271` n `8`; equity avg `0.0064` n `127`; fx avg `0.0044` n `6`; index avg `-0.0018` n `26`; metal avg `0.0108` n `20`; unknown avg `0.046` n `793`
- 1h: commodity avg `0.0468` n `12`; crypto_alt avg `-0.0274` n `231`; crypto_major avg `0.0702` n `8`; equity avg `0.041` n `127`; fx avg `0.0142` n `6`; index avg `-0.004` n `26`; metal avg `0.0043` n `20`; unknown avg `0.1064` n `793`
- 4h: commodity avg `-0.0068` n `12`; crypto_alt avg `-0.1096` n `231`; crypto_major avg `-0.0965` n `8`; equity avg `0.1132` n `127`; fx avg `0.0054` n `6`; index avg `0.0128` n `26`; metal avg `0.0109` n `20`; unknown avg `0.1218` n `761`
- 24h: commodity avg `0.0193` n `12`; crypto_alt avg `-1.9891` n `231`; crypto_major avg `-2.5189` n `8`; equity avg `-1.4309` n `127`; fx avg `-0.0174` n `6`; index avg `-0.15` n `26`; metal avg `-0.579` n `20`; unknown avg `-0.3989` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
