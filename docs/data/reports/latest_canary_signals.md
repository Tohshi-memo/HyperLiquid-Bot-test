# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T00:07:19.749794+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0926` n `12`; crypto_alt avg `0.2268` n `228`; crypto_major avg `0.0666` n `8`; equity avg `-0.0378` n `69`; fx avg `0.0292` n `6`; index avg `-0.0274` n `23`; metal avg `0.063` n `18`; unknown avg `0.3813` n `417`
- 1h: commodity avg `-0.14` n `12`; crypto_alt avg `0.2701` n `228`; crypto_major avg `-0.0615` n `8`; equity avg `0.0864` n `69`; fx avg `0.0491` n `6`; index avg `-0.0202` n `23`; metal avg `0.0357` n `18`; unknown avg `0.4551` n `417`
- 4h: commodity avg `-0.3422` n `12`; crypto_alt avg `0.5887` n `228`; crypto_major avg `0.3836` n `8`; equity avg `0.6153` n `69`; fx avg `0.0546` n `6`; index avg `-0.0625` n `23`; metal avg `0.0773` n `18`; unknown avg `0.0254` n `417`
- 24h: commodity avg `0.4386` n `12`; crypto_alt avg `-1.6596` n `228`; crypto_major avg `0.2903` n `8`; equity avg `2.768` n `69`; fx avg `0.0193` n `6`; index avg `1.0069` n `23`; metal avg `0.6817` n `18`; unknown avg `0.1636` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1835`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
