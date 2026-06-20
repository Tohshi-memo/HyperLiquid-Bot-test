# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T14:22:28.881229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.038` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.039` n `12`; crypto_alt avg `0.1234` n `228`; crypto_major avg `0.0758` n `8`; equity avg `0.0617` n `78`; fx avg `0.0274` n `6`; index avg `0.0038` n `23`; metal avg `-0.0184` n `18`; unknown avg `-0.1474` n `701`
- 1h: commodity avg `-0.0732` n `12`; crypto_alt avg `-0.5684` n `228`; crypto_major avg `-0.5692` n `8`; equity avg `-0.0979` n `78`; fx avg `0.0275` n `6`; index avg `-0.0237` n `23`; metal avg `-0.0474` n `18`; unknown avg `-0.204` n `701`
- 4h: commodity avg `0.2587` n `12`; crypto_alt avg `-1.3311` n `228`; crypto_major avg `-1.0644` n `8`; equity avg `-0.3482` n `78`; fx avg `0.0216` n `6`; index avg `-0.0264` n `23`; metal avg `-0.0529` n `18`; unknown avg `-0.422` n `573`
- 24h: commodity avg `0.7598` n `12`; crypto_alt avg `-4.1184` n `228`; crypto_major avg `-4.3375` n `8`; equity avg `0.8458` n `78`; fx avg `-0.0579` n `6`; index avg `0.2661` n `23`; metal avg `-4.1631` n `18`; unknown avg `-0.4259` n `492`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
