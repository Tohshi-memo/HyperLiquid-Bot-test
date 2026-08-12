# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T16:52:24.461799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.05` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `-0.0558` n `230`; crypto_major avg `-0.0451` n `8`; equity avg `0.006` n `113`; fx avg `-0.004` n `6`; index avg `0.0083` n `25`; metal avg `-0.0805` n `20`; unknown avg `0.0071` n `786`
- 1h: commodity avg `-0.0497` n `12`; crypto_alt avg `-0.0966` n `230`; crypto_major avg `-0.0786` n `8`; equity avg `0.2567` n `113`; fx avg `-0.0089` n `6`; index avg `0.0289` n `25`; metal avg `-0.1018` n `20`; unknown avg `0.0215` n `786`
- 4h: commodity avg `-0.055` n `12`; crypto_alt avg `-0.7481` n `230`; crypto_major avg `-0.5053` n `8`; equity avg `0.5725` n `113`; fx avg `-0.0287` n `6`; index avg `0.0145` n `25`; metal avg `-0.2964` n `20`; unknown avg `0.077` n `786`
- 24h: commodity avg `0.0941` n `12`; crypto_alt avg `-0.233` n `230`; crypto_major avg `0.9799` n `8`; equity avg `3.5229` n `113`; fx avg `0.0332` n `6`; index avg `0.3797` n `25`; metal avg `0.1445` n `20`; unknown avg `0.0111` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2276`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2042`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1961`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
