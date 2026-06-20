# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T14:52:29.745119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2015` n `12`; crypto_alt avg `0.8535` n `228`; crypto_major avg `0.9208` n `8`; equity avg `0.2703` n `78`; fx avg `0.0015` n `6`; index avg `0.0174` n `23`; metal avg `0.0921` n `18`; unknown avg `1.0572` n `701`
- 1h: commodity avg `-0.1302` n `12`; crypto_alt avg `0.6185` n `228`; crypto_major avg `0.6865` n `8`; equity avg `0.2391` n `78`; fx avg `0.0326` n `6`; index avg `0.0099` n `23`; metal avg `0.076` n `18`; unknown avg `0.2881` n `701`
- 4h: commodity avg `0.0535` n `12`; crypto_alt avg `0.0351` n `228`; crypto_major avg `0.0704` n `8`; equity avg `-0.0074` n `78`; fx avg `0.0248` n `6`; index avg `0.0025` n `23`; metal avg `0.035` n `18`; unknown avg `0.5956` n `573`
- 24h: commodity avg `0.5316` n `12`; crypto_alt avg `-3.0422` n `228`; crypto_major avg `-3.2678` n `8`; equity avg `1.1712` n `78`; fx avg `-0.0564` n `6`; index avg `0.2874` n `23`; metal avg `-4.0689` n `18`; unknown avg `-0.27` n `492`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
