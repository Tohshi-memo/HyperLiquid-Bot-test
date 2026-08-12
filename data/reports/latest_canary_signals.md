# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T19:07:37.908335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `12`; crypto_alt avg `-0.0455` n `230`; crypto_major avg `0.0134` n `8`; equity avg `-0.011` n `113`; fx avg `-0.0032` n `6`; index avg `0.0032` n `25`; metal avg `0.0037` n `20`; unknown avg `-0.0224` n `786`
- 1h: commodity avg `0.012` n `12`; crypto_alt avg `-0.1919` n `230`; crypto_major avg `-0.0946` n `8`; equity avg `-0.0425` n `113`; fx avg `-0.0047` n `6`; index avg `0.021` n `25`; metal avg `0.0724` n `20`; unknown avg `-0.1162` n `786`
- 4h: commodity avg `-0.011` n `12`; crypto_alt avg `-0.1859` n `230`; crypto_major avg `0.1217` n `8`; equity avg `0.5416` n `113`; fx avg `-0.0035` n `6`; index avg `0.041` n `25`; metal avg `-0.1069` n `20`; unknown avg `0.1918` n `786`
- 24h: commodity avg `0.0565` n `12`; crypto_alt avg `-0.2049` n `230`; crypto_major avg `0.9041` n `8`; equity avg `3.9535` n `113`; fx avg `0.0238` n `6`; index avg `0.4695` n `25`; metal avg `0.3032` n `20`; unknown avg `0.1766` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2246`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1981`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1925`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
