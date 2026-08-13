# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T03:22:25.526972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0369` n `12`; crypto_alt avg `0.1077` n `230`; crypto_major avg `0.082` n `8`; equity avg `-0.0065` n `113`; fx avg `0.0039` n `6`; index avg `0.0043` n `25`; metal avg `-0.0063` n `20`; unknown avg `0.106` n `786`
- 1h: commodity avg `0.0399` n `12`; crypto_alt avg `0.2456` n `230`; crypto_major avg `0.3449` n `8`; equity avg `-0.0221` n `113`; fx avg `0.0118` n `6`; index avg `0.0046` n `25`; metal avg `-0.0451` n `20`; unknown avg `0.8745` n `786`
- 4h: commodity avg `-0.1062` n `12`; crypto_alt avg `0.6461` n `230`; crypto_major avg `0.6113` n `8`; equity avg `0.463` n `113`; fx avg `-0.0214` n `6`; index avg `0.0574` n `25`; metal avg `-0.0417` n `20`; unknown avg `-0.0136` n `786`
- 24h: commodity avg `-0.2523` n `12`; crypto_alt avg `-1.3128` n `230`; crypto_major avg `-0.1567` n `8`; equity avg `2.454` n `113`; fx avg `-0.0677` n `6`; index avg `0.2794` n `25`; metal avg `-0.1027` n `20`; unknown avg `-0.001` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.24`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2053`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1886`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
