# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T17:07:24.683871+00:00`
- Correlation status: `ready`
- Asset price records: `664`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1235` n `12`; crypto_alt avg `0.2107` n `228`; crypto_major avg `0.1309` n `8`; equity avg `0.0985` n `65`; fx avg `0.0026` n `5`; index avg `0.0462` n `23`; metal avg `0.0604` n `18`; unknown avg `0.0073` n `375`
- 1h: commodity avg `-0.1412` n `12`; crypto_alt avg `0.4106` n `228`; crypto_major avg `0.0143` n `8`; equity avg `0.0024` n `65`; fx avg `0.0102` n `5`; index avg `0.1277` n `23`; metal avg `0.1295` n `18`; unknown avg `-0.1202` n `375`
- 4h: commodity avg `0.2397` n `12`; crypto_alt avg `1.498` n `228`; crypto_major avg `0.6297` n `8`; equity avg `0.9284` n `65`; fx avg `-0.018` n `5`; index avg `0.4771` n `23`; metal avg `-0.1188` n `18`; unknown avg `0.078` n `375`
- 24h: commodity avg `0.306` n `12`; crypto_alt avg `2.8468` n `228`; crypto_major avg `0.3836` n `8`; equity avg `2.4952` n `65`; fx avg `0.1387` n `5`; index avg `1.2083` n `23`; metal avg `0.1056` n `18`; unknown avg `0.1286` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1207`, n `656`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1164`, n `656`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1149`, n `660`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.103`, n `656`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0986`, n `660`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0968`, n `656`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `660`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `660`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0734`, n `660`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.072`, n `660`, weak_sample_signal
