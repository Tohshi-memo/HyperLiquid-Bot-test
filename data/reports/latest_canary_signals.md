# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T19:22:20.952362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0286` n `12`; crypto_alt avg `-0.515` n `228`; crypto_major avg `-0.2045` n `8`; equity avg `0.0721` n `69`; fx avg `0.0068` n `6`; index avg `0.0101` n `23`; metal avg `0.0359` n `18`; unknown avg `-0.4688` n `419`
- 1h: commodity avg `0.0725` n `12`; crypto_alt avg `-1.0654` n `228`; crypto_major avg `-0.6495` n `8`; equity avg `-0.3001` n `69`; fx avg `0.013` n `6`; index avg `-0.0674` n `23`; metal avg `0.0716` n `18`; unknown avg `-0.1599` n `419`
- 4h: commodity avg `-0.0206` n `12`; crypto_alt avg `-0.3556` n `228`; crypto_major avg `-0.2068` n `8`; equity avg `0.0584` n `69`; fx avg `0.0051` n `6`; index avg `0.0845` n `23`; metal avg `-0.3326` n `18`; unknown avg `-0.2117` n `418`
- 24h: commodity avg `-0.7967` n `12`; crypto_alt avg `-0.0771` n `228`; crypto_major avg `0.6073` n `8`; equity avg `1.135` n `69`; fx avg `0.217` n `6`; index avg `-0.0573` n `23`; metal avg `0.2986` n `18`; unknown avg `0.5027` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1892`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
