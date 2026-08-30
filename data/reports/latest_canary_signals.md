# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T10:22:24.787595+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `0.1238` n `231`; crypto_major avg `0.0819` n `8`; equity avg `0.0152` n `128`; fx avg `-0.0043` n `6`; index avg `-0.0056` n `26`; metal avg `0.0045` n `20`; unknown avg `-0.1273` n `793`
- 1h: commodity avg `-0.0114` n `12`; crypto_alt avg `0.2691` n `231`; crypto_major avg `-0.0301` n `8`; equity avg `0.0034` n `128`; fx avg `0.0012` n `6`; index avg `0.017` n `26`; metal avg `0.0026` n `20`; unknown avg `-0.1834` n `793`
- 4h: commodity avg `-0.0126` n `12`; crypto_alt avg `0.1508` n `231`; crypto_major avg `-0.1765` n `8`; equity avg `-0.0096` n `128`; fx avg `-0.0036` n `6`; index avg `-0.001` n `26`; metal avg `0.0022` n `20`; unknown avg `-0.2926` n `789`
- 24h: commodity avg `-0.0281` n `12`; crypto_alt avg `1.2635` n `231`; crypto_major avg `0.7338` n `8`; equity avg `0.2488` n `128`; fx avg `0.0113` n `6`; index avg `0.0706` n `26`; metal avg `0.0802` n `20`; unknown avg `0.6523` n `716`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
