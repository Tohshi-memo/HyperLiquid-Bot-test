# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T21:07:22.895433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0445` n `12`; crypto_alt avg `-0.2135` n `228`; crypto_major avg `-0.2622` n `8`; equity avg `0.0046` n `74`; fx avg `0.0161` n `6`; index avg `0.1163` n `23`; metal avg `0.0085` n `18`; unknown avg `0.0588` n `516`
- 1h: commodity avg `-0.2305` n `12`; crypto_alt avg `0.4265` n `228`; crypto_major avg `0.4073` n `8`; equity avg `0.172` n `74`; fx avg `-0.0191` n `6`; index avg `0.2126` n `23`; metal avg `0.0189` n `18`; unknown avg `0.5066` n `516`
- 4h: commodity avg `0.177` n `12`; crypto_alt avg `-1.4359` n `228`; crypto_major avg `-0.8061` n `8`; equity avg `-0.7084` n `74`; fx avg `0.0155` n `6`; index avg `-0.1669` n `23`; metal avg `-0.3224` n `18`; unknown avg `-0.0742` n `516`
- 24h: commodity avg `0.3074` n `12`; crypto_alt avg `1.8405` n `228`; crypto_major avg `2.944` n `8`; equity avg `1.1317` n `74`; fx avg `-0.0671` n `6`; index avg `0.2569` n `23`; metal avg `0.3034` n `18`; unknown avg `-4.5822` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
