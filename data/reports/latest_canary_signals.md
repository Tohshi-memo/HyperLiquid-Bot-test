# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T19:42:44.911197+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0391` n `12`; crypto_alt avg `-0.0388` n `228`; crypto_major avg `-0.0901` n `8`; equity avg `0.0317` n `65`; fx avg `0.0261` n `5`; index avg `-0.0256` n `23`; metal avg `0.1077` n `18`; unknown avg `0.1456` n `375`
- 1h: commodity avg `0.0513` n `12`; crypto_alt avg `-0.1281` n `228`; crypto_major avg `-0.0407` n `8`; equity avg `0.0894` n `65`; fx avg `0.0414` n `5`; index avg `-0.0036` n `23`; metal avg `0.0212` n `18`; unknown avg `-0.1298` n `375`
- 4h: commodity avg `-0.2937` n `12`; crypto_alt avg `1.8675` n `228`; crypto_major avg `1.523` n `8`; equity avg `0.6274` n `65`; fx avg `0.068` n `5`; index avg `0.2819` n `23`; metal avg `0.4272` n `18`; unknown avg `0.2068` n `375`
- 24h: commodity avg `-0.0485` n `12`; crypto_alt avg `3.1201` n `228`; crypto_major avg `1.4334` n `8`; equity avg `3.3443` n `65`; fx avg `0.2166` n `5`; index avg `1.4608` n `23`; metal avg `0.8486` n `18`; unknown avg `1.1074` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1259`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1224`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0945`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0936`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0639`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
