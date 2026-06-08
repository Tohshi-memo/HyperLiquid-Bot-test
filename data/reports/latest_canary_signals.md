# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T23:07:20.343385+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `12`; crypto_alt avg `0.1406` n `228`; crypto_major avg `0.2631` n `8`; equity avg `0.071` n `74`; fx avg `0.005` n `6`; index avg `-0.0001` n `23`; metal avg `0.0172` n `18`; unknown avg `0.0713` n `517`
- 1h: commodity avg `-0.0189` n `12`; crypto_alt avg `-0.3476` n `228`; crypto_major avg `0.0348` n `8`; equity avg `0.0046` n `74`; fx avg `0.046` n `6`; index avg `-0.1359` n `23`; metal avg `0.0238` n `18`; unknown avg `-0.6509` n `517`
- 4h: commodity avg `0.0745` n `12`; crypto_alt avg `-0.7549` n `228`; crypto_major avg `-0.0859` n `8`; equity avg `-0.1955` n `74`; fx avg `-0.0022` n `6`; index avg `-0.1269` n `23`; metal avg `-0.0199` n `18`; unknown avg `-0.9685` n `517`
- 24h: commodity avg `-0.7427` n `12`; crypto_alt avg `1.3007` n `228`; crypto_major avg `2.1259` n `8`; equity avg `2.0954` n `74`; fx avg `-0.2721` n `6`; index avg `1.0224` n `23`; metal avg `0.1648` n `18`; unknown avg `-2.8567` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
