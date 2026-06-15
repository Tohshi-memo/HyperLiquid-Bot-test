# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T06:37:36.228572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.79` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0282` n `12`; crypto_alt avg `-0.0384` n `228`; crypto_major avg `-0.1297` n `8`; equity avg `-0.0235` n `74`; fx avg `0.0135` n `6`; index avg `-0.1571` n `23`; metal avg `-0.019` n `18`; unknown avg `0.7975` n `689`
- 1h: commodity avg `-0.0356` n `12`; crypto_alt avg `-0.099` n `228`; crypto_major avg `-0.0583` n `8`; equity avg `-0.0052` n `74`; fx avg `0.0321` n `6`; index avg `-0.0414` n `23`; metal avg `-0.2558` n `18`; unknown avg `-0.2479` n `529`
- 4h: commodity avg `0.1654` n `12`; crypto_alt avg `0.4194` n `228`; crypto_major avg `-0.1112` n `8`; equity avg `0.0579` n `74`; fx avg `0.039` n `6`; index avg `-0.1703` n `23`; metal avg `-0.5999` n `18`; unknown avg `0.0138` n `529`
- 24h: commodity avg `-0.86` n `12`; crypto_alt avg `3.1132` n `228`; crypto_major avg `2.8802` n `8`; equity avg `1.7474` n `74`; fx avg `0.0596` n `6`; index avg `0.7371` n `23`; metal avg `1.6908` n `18`; unknown avg `1.422` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
