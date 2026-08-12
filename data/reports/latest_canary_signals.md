# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T23:22:26.171149+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `0.0779` n `230`; crypto_major avg `0.0441` n `8`; equity avg `0.0551` n `113`; fx avg `-0.004` n `6`; index avg `0.0172` n `25`; metal avg `0.0256` n `20`; unknown avg `0.1996` n `786`
- 1h: commodity avg `0.0126` n `12`; crypto_alt avg `0.081` n `230`; crypto_major avg `-0.1191` n `8`; equity avg `0.16` n `113`; fx avg `0.0018` n `6`; index avg `0.0174` n `25`; metal avg `0.0396` n `20`; unknown avg `-0.0854` n `786`
- 4h: commodity avg `-0.0729` n `12`; crypto_alt avg `-0.7241` n `230`; crypto_major avg `-0.5026` n `8`; equity avg `-0.1559` n `113`; fx avg `-0.0105` n `6`; index avg `0.009` n `25`; metal avg `-0.0921` n `20`; unknown avg `-0.2981` n `786`
- 24h: commodity avg `-0.0123` n `12`; crypto_alt avg `-1.5355` n `230`; crypto_major avg `-0.5212` n `8`; equity avg `2.8716` n `113`; fx avg `0.0202` n `6`; index avg `0.4151` n `25`; metal avg `0.1337` n `20`; unknown avg `-0.0637` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2358`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1885`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
