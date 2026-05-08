# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T16:07:13.186752+00:00`
- Correlation status: `ready`
- Asset price records: `660`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0227` n `12`; crypto_alt avg `0.1662` n `228`; crypto_major avg `0.0255` n `8`; equity avg `0.0976` n `65`; fx avg `-0.0129` n `5`; index avg `0.037` n `23`; metal avg `0.0394` n `18`; unknown avg `0.0155` n `375`
- 1h: commodity avg `0.115` n `12`; crypto_alt avg `0.3557` n `228`; crypto_major avg `0.2012` n `8`; equity avg `-0.0557` n `65`; fx avg `-0.003` n `5`; index avg `0.0125` n `23`; metal avg `-0.3427` n `18`; unknown avg `-0.118` n `375`
- 4h: commodity avg `0.6683` n `12`; crypto_alt avg `0.8138` n `228`; crypto_major avg `0.2827` n `8`; equity avg `1.1133` n `65`; fx avg `-0.049` n `5`; index avg `0.4355` n `23`; metal avg `-0.3413` n `18`; unknown avg `-0.0011` n `375`
- 24h: commodity avg `1.0451` n `12`; crypto_alt avg `3.1546` n `228`; crypto_major avg `0.6068` n `8`; equity avg `2.0735` n `65`; fx avg `0.1453` n `5`; index avg `0.8085` n `23`; metal avg `-0.0601` n `18`; unknown avg `0.6238` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1206`, n `652`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1182`, n `656`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1164`, n `652`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.101`, n `656`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.101`, n `652`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0966`, n `652`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `656`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0863`, n `656`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `656`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0718`, n `656`, weak_sample_signal
