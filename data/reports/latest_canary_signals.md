# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T05:07:25.434426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0332` n `12`; crypto_alt avg `0.417` n `228`; crypto_major avg `0.5246` n `8`; equity avg `0.0908` n `74`; fx avg `-0.0054` n `6`; index avg `0.0388` n `23`; metal avg `0.0858` n `18`; unknown avg `1.2954` n `424`
- 1h: commodity avg `0.115` n `12`; crypto_alt avg `0.4536` n `228`; crypto_major avg `0.1372` n `8`; equity avg `0.2871` n `74`; fx avg `-0.0233` n `6`; index avg `0.1534` n `23`; metal avg `0.1019` n `18`; unknown avg `0.0278` n `424`
- 4h: commodity avg `0.3626` n `12`; crypto_alt avg `-0.901` n `228`; crypto_major avg `-0.7036` n `8`; equity avg `0.5865` n `74`; fx avg `0.01` n `6`; index avg `0.1212` n `23`; metal avg `-0.1797` n `18`; unknown avg `-0.8168` n `424`
- 24h: commodity avg `-0.1152` n `12`; crypto_alt avg `-4.0225` n `228`; crypto_major avg `-3.7418` n `8`; equity avg `-1.2914` n `73`; fx avg `0.1769` n `6`; index avg `-0.4598` n `23`; metal avg `-0.5746` n `18`; unknown avg `-1.5347` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
