# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T12:52:28.205228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4271` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `0.0671` n `228`; crypto_major avg `0.1827` n `8`; equity avg `-0.022` n `74`; fx avg `0.0017` n `6`; index avg `0.0093` n `23`; metal avg `-0.1721` n `18`; unknown avg `0.0876` n `517`
- 1h: commodity avg `0.2004` n `12`; crypto_alt avg `0.22` n `228`; crypto_major avg `0.2068` n `8`; equity avg `0.2725` n `74`; fx avg `-0.0107` n `6`; index avg `0.1979` n `23`; metal avg `-0.0256` n `18`; unknown avg `-2.4198` n `517`
- 4h: commodity avg `-0.9658` n `12`; crypto_alt avg `1.8102` n `228`; crypto_major avg `1.4613` n `8`; equity avg `1.5077` n `74`; fx avg `0.0492` n `6`; index avg `0.7442` n `23`; metal avg `0.9319` n `18`; unknown avg `-1.9972` n `517`
- 24h: commodity avg `-0.3206` n `12`; crypto_alt avg `2.7365` n `228`; crypto_major avg `3.5926` n `8`; equity avg `2.3311` n `74`; fx avg `-0.2939` n `6`; index avg `1.1284` n `23`; metal avg `0.2926` n `18`; unknown avg `-3.326` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
