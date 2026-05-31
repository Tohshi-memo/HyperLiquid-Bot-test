# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T02:37:15.691334+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `12`; crypto_alt avg `-0.4506` n `228`; crypto_major avg `-0.2941` n `8`; equity avg `0.0032` n `69`; fx avg `-0.0165` n `6`; index avg `-0.0352` n `23`; metal avg `-0.0001` n `18`; unknown avg `0.0912` n `419`
- 1h: commodity avg `-0.0709` n `12`; crypto_alt avg `-0.2564` n `228`; crypto_major avg `-0.2434` n `8`; equity avg `0.0128` n `69`; fx avg `0.0175` n `6`; index avg `-0.0425` n `23`; metal avg `-0.0534` n `18`; unknown avg `0.8418` n `419`
- 4h: commodity avg `-0.001` n `12`; crypto_alt avg `0.4899` n `228`; crypto_major avg `0.7617` n `8`; equity avg `0.297` n `69`; fx avg `-0.0072` n `6`; index avg `-0.0025` n `23`; metal avg `-0.0519` n `18`; unknown avg `-0.0855` n `419`
- 24h: commodity avg `-0.0469` n `12`; crypto_alt avg `-0.1967` n `228`; crypto_major avg `1.9692` n `8`; equity avg `0.9319` n `69`; fx avg `0.0322` n `6`; index avg `0.064` n `23`; metal avg `-0.0611` n `18`; unknown avg `1.312` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
