# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T22:07:38.999736+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1177` n `12`; crypto_alt avg `-0.4724` n `228`; crypto_major avg `-0.4512` n `8`; equity avg `-0.1345` n `74`; fx avg `0.3012` n `6`; index avg `-0.1006` n `23`; metal avg `-0.1504` n `18`; unknown avg `-0.0351` n `517`
- 1h: commodity avg `-0.1627` n `12`; crypto_alt avg `-0.4744` n `228`; crypto_major avg `-0.4632` n `8`; equity avg `-0.1626` n `74`; fx avg `-0.0922` n `6`; index avg `-0.011` n `23`; metal avg `-0.1045` n `18`; unknown avg `-0.0202` n `517`
- 4h: commodity avg `-0.0625` n `12`; crypto_alt avg `-0.64` n `228`; crypto_major avg `-0.1991` n `8`; equity avg `-0.5878` n `74`; fx avg `-0.0745` n `6`; index avg `-0.1528` n `23`; metal avg `-0.1729` n `18`; unknown avg `-0.1624` n `517`
- 24h: commodity avg `-0.9005` n `12`; crypto_alt avg `3.0054` n `228`; crypto_major avg `3.6706` n `8`; equity avg `2.5433` n `74`; fx avg `-0.3179` n `6`; index avg `1.2708` n `23`; metal avg `0.2865` n `18`; unknown avg `-1.9979` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
