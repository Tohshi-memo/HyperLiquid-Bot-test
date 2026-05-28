# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T08:31:56.878986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0915` n `12`; crypto_alt avg `-0.1885` n `228`; crypto_major avg `-0.1596` n `8`; equity avg `-0.1137` n `67`; fx avg `-0.0044` n `6`; index avg `-0.0584` n `23`; metal avg `-0.1735` n `18`; unknown avg `-0.0404` n `419`
- 1h: commodity avg `-0.0431` n `12`; crypto_alt avg `-0.625` n `228`; crypto_major avg `-0.5714` n `8`; equity avg `0.0033` n `67`; fx avg `-0.0216` n `6`; index avg `0.0154` n `23`; metal avg `-0.0945` n `18`; unknown avg `-0.1984` n `419`
- 4h: commodity avg `-0.4784` n `12`; crypto_alt avg `-0.427` n `228`; crypto_major avg `-0.0707` n `8`; equity avg `1.1841` n `67`; fx avg `0.0319` n `6`; index avg `0.5005` n `23`; metal avg `0.7896` n `18`; unknown avg `-0.121` n `409`
- 24h: commodity avg `0.7414` n `12`; crypto_alt avg `-5.4073` n `228`; crypto_major avg `-4.0535` n `8`; equity avg `-1.5144` n `67`; fx avg `-0.1192` n `6`; index avg `-1.0114` n `23`; metal avg `-1.6041` n `18`; unknown avg `-1.6838` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1714`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
