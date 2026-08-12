# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T22:56:46.438116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `0.0247` n `230`; crypto_major avg `0.0003` n `8`; equity avg `0.0616` n `113`; fx avg `0.0034` n `6`; index avg `0.0132` n `25`; metal avg `0.0183` n `20`; unknown avg `-0.0896` n `786`
- 1h: commodity avg `-0.0158` n `12`; crypto_alt avg `0.0036` n `230`; crypto_major avg `-0.1011` n `8`; equity avg `-0.0475` n `113`; fx avg `0.0016` n `6`; index avg `-0.0067` n `25`; metal avg `-0.0451` n `20`; unknown avg `-0.1354` n `786`
- 4h: commodity avg `-0.0965` n `12`; crypto_alt avg `-0.9168` n `230`; crypto_major avg `-0.5227` n `8`; equity avg `-0.3156` n `113`; fx avg `-0.0061` n `6`; index avg `-0.0087` n `25`; metal avg `-0.1316` n `20`; unknown avg `-0.3821` n `786`
- 24h: commodity avg `-0.024` n `12`; crypto_alt avg `-1.5886` n `230`; crypto_major avg `-0.5813` n `8`; equity avg `2.7833` n `113`; fx avg `0.0219` n `6`; index avg `0.4003` n `25`; metal avg `0.0964` n `20`; unknown avg `-0.1316` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2339`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1945`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1864`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1815`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
