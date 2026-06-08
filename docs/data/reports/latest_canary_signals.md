# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T15:07:28.311520+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5444` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.1726` n `12`; crypto_alt avg `0.2797` n `228`; crypto_major avg `0.2848` n `8`; equity avg `0.1885` n `74`; fx avg `0.0116` n `6`; index avg `0.2061` n `23`; metal avg `0.2427` n `18`; unknown avg `-0.0951` n `517`
- 1h: commodity avg `0.011` n `12`; crypto_alt avg `0.6092` n `228`; crypto_major avg `0.6564` n `8`; equity avg `1.1038` n `74`; fx avg `-0.0079` n `6`; index avg `0.4378` n `23`; metal avg `0.4522` n `18`; unknown avg `-0.2733` n `517`
- 4h: commodity avg `-0.6484` n `12`; crypto_alt avg `1.2855` n `228`; crypto_major avg `1.896` n `8`; equity avg `1.9907` n `74`; fx avg `0.0017` n `6`; index avg `0.9889` n `23`; metal avg `0.6551` n `18`; unknown avg `-1.726` n `517`
- 24h: commodity avg `-0.4265` n `12`; crypto_alt avg `2.4729` n `228`; crypto_major avg `4.1226` n `8`; equity avg `2.856` n `74`; fx avg `-0.2668` n `6`; index avg `1.4259` n `23`; metal avg `0.1059` n `18`; unknown avg `-2.9822` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
