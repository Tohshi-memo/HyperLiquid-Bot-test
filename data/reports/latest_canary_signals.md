# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T00:07:25.302153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0485` n `12`; crypto_alt avg `0.2206` n `230`; crypto_major avg `0.135` n `8`; equity avg `0.3106` n `113`; fx avg `-0.0372` n `6`; index avg `0.067` n `25`; metal avg `0.0553` n `20`; unknown avg `0.0391` n `786`
- 1h: commodity avg `-0.036` n `12`; crypto_alt avg `0.4742` n `230`; crypto_major avg `0.3026` n `8`; equity avg `0.3981` n `113`; fx avg `-0.0371` n `6`; index avg `0.0656` n `25`; metal avg `0.1021` n `20`; unknown avg `0.0546` n `786`
- 4h: commodity avg `-0.0765` n `12`; crypto_alt avg `-0.3921` n `230`; crypto_major avg `-0.1837` n `8`; equity avg `0.196` n `113`; fx avg `-0.0469` n `6`; index avg `0.0451` n `25`; metal avg `0.031` n `20`; unknown avg `-0.2057` n `786`
- 24h: commodity avg `-0.0989` n `12`; crypto_alt avg `-1.167` n `230`; crypto_major avg `-0.3664` n `8`; equity avg `3.1432` n `113`; fx avg `-0.0192` n `6`; index avg `0.4574` n `25`; metal avg `0.224` n `20`; unknown avg `-0.0113` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.238`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2005`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1892`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1826`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
