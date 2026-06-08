# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T03:22:23.661846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `0.2579` n `228`; crypto_major avg `0.3108` n `8`; equity avg `-0.0778` n `74`; fx avg `-0.0027` n `6`; index avg `-0.0014` n `23`; metal avg `0.042` n `18`; unknown avg `-0.0347` n `517`
- 1h: commodity avg `0.0015` n `12`; crypto_alt avg `0.0805` n `228`; crypto_major avg `0.349` n `8`; equity avg `0.3579` n `74`; fx avg `-0.0169` n `6`; index avg `0.2127` n `23`; metal avg `0.0081` n `18`; unknown avg `-0.1375` n `517`
- 4h: commodity avg `0.3064` n `12`; crypto_alt avg `0.2492` n `228`; crypto_major avg `1.0497` n `8`; equity avg `1.0932` n `74`; fx avg `-0.0382` n `6`; index avg `0.5795` n `23`; metal avg `-0.2515` n `18`; unknown avg `-0.328` n `516`
- 24h: commodity avg `0.4663` n `12`; crypto_alt avg `1.1397` n `228`; crypto_major avg `3.5969` n `8`; equity avg `1.7317` n `74`; fx avg `-0.0945` n `6`; index avg `0.4836` n `23`; metal avg `-0.3187` n `18`; unknown avg `-5.4205` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
