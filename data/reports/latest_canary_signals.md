# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T18:22:23.381641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3484` n `12`; crypto_alt avg `0.0055` n `228`; crypto_major avg `0.1296` n `8`; equity avg `0.1753` n `67`; fx avg `0.0013` n `6`; index avg `0.0601` n `23`; metal avg `0.2332` n `18`; unknown avg `-0.1206` n `418`
- 1h: commodity avg `-0.38` n `12`; crypto_alt avg `-0.4566` n `228`; crypto_major avg `-0.2068` n `8`; equity avg `0.2381` n `67`; fx avg `-0.0117` n `6`; index avg `0.0895` n `23`; metal avg `0.15` n `18`; unknown avg `-0.2395` n `418`
- 4h: commodity avg `-0.1507` n `12`; crypto_alt avg `-0.0629` n `228`; crypto_major avg `-0.0936` n `8`; equity avg `-0.0167` n `67`; fx avg `-0.038` n `6`; index avg `0.066` n `23`; metal avg `-0.0156` n `18`; unknown avg `-0.5505` n `418`
- 24h: commodity avg `-1.4266` n `12`; crypto_alt avg `-1.3694` n `228`; crypto_major avg `-1.2033` n `8`; equity avg `-0.4596` n `67`; fx avg `-0.0716` n `6`; index avg `-0.4967` n `23`; metal avg `-0.7008` n `18`; unknown avg `-1.0732` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
