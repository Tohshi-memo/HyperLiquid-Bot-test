# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T07:22:25.436159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.54` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0043` n `12`; crypto_alt avg `0.0153` n `231`; crypto_major avg `-0.008` n `8`; equity avg `0.0088` n `127`; fx avg `0.0017` n `6`; index avg `0.0021` n `26`; metal avg `0.0124` n `20`; unknown avg `-0.0037` n `793`
- 1h: commodity avg `0.0424` n `12`; crypto_alt avg `0.2249` n `231`; crypto_major avg `0.28` n `8`; equity avg `0.0566` n `127`; fx avg `-0.0002` n `6`; index avg `0.0013` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.0665` n `793`
- 4h: commodity avg `0.005` n `12`; crypto_alt avg `-0.3396` n `231`; crypto_major avg `-0.227` n `8`; equity avg `0.0982` n `127`; fx avg `0.0047` n `6`; index avg `0.0131` n `26`; metal avg `0.0205` n `20`; unknown avg `-0.0297` n `761`
- 24h: commodity avg `-0.0361` n `12`; crypto_alt avg `-1.9385` n `231`; crypto_major avg `-2.4968` n `8`; equity avg `-1.4903` n `127`; fx avg `-0.0113` n `6`; index avg `-0.1442` n `26`; metal avg `-0.5479` n `20`; unknown avg `-0.4388` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
