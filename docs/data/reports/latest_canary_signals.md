# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T06:07:18.996950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `0.0826` n `228`; crypto_major avg `0.1098` n `8`; equity avg `0.0091` n `65`; fx avg `-0.0017` n `5`; index avg `0.006` n `23`; metal avg `0.0048` n `18`; unknown avg `-0.0201` n `356`
- 1h: commodity avg `0.0231` n `12`; crypto_alt avg `0.3223` n `228`; crypto_major avg `0.292` n `8`; equity avg `0.0265` n `65`; fx avg `0.0179` n `5`; index avg `-0.0151` n `23`; metal avg `0.0217` n `18`; unknown avg `0.0798` n `356`
- 4h: commodity avg `0.1624` n `12`; crypto_alt avg `0.2169` n `228`; crypto_major avg `0.0469` n `8`; equity avg `0.018` n `65`; fx avg `-0.0021` n `5`; index avg `0.0284` n `23`; metal avg `0.0167` n `18`; unknown avg `-0.1323` n `355`
- 24h: commodity avg `0.0393` n `12`; crypto_alt avg `5.0523` n `228`; crypto_major avg `3.0815` n `8`; equity avg `3.5065` n `65`; fx avg `0.0192` n `5`; index avg `1.313` n `23`; metal avg `-0.3942` n `18`; unknown avg `1.4592` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
