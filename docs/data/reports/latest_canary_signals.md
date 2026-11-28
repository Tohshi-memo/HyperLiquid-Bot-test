# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T09:22:26.779103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0011` n `13`; crypto_alt avg `-0.0625` n `239`; crypto_major avg `0.0122` n `8`; equity avg `-0.0051` n `168`; fx avg `-0.0029` n `6`; index avg `-0.0032` n `27`; metal avg `-0.0022` n `20`; unknown avg `0.3032` n `1265`
- 1h: commodity avg `-0.0146` n `13`; crypto_alt avg `0.1052` n `239`; crypto_major avg `-0.1383` n `8`; equity avg `-0.0529` n `168`; fx avg `0.0061` n `6`; index avg `-0.0139` n `27`; metal avg `-0.0013` n `20`; unknown avg `-0.1314` n `1231`
- 4h: commodity avg `-0.0376` n `13`; crypto_alt avg `-0.4202` n `239`; crypto_major avg `-0.3422` n `8`; equity avg `-0.0595` n `168`; fx avg `-0.0051` n `6`; index avg `-0.0296` n `27`; metal avg `0.0056` n `20`; unknown avg `0.2859` n `1193`
- 24h: commodity avg `-0.5941` n `13`; crypto_alt avg `-3.083` n `239`; crypto_major avg `-2.8738` n `8`; equity avg `-0.8509` n `168`; fx avg `-0.0534` n `6`; index avg `-0.0286` n `27`; metal avg `-0.357` n `20`; unknown avg `190.9298` n `1087`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
