# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T20:22:31.650134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `-0.1099` n `228`; crypto_major avg `-0.2027` n `8`; equity avg `0.0185` n `85`; fx avg `0.0046` n `6`; index avg `0.0037` n `23`; metal avg `-0.0155` n `20`; unknown avg `-0.0871` n `709`
- 1h: commodity avg `-0.0269` n `12`; crypto_alt avg `0.0029` n `228`; crypto_major avg `-0.075` n `8`; equity avg `0.1861` n `85`; fx avg `0.0182` n `6`; index avg `0.0348` n `23`; metal avg `-0.0069` n `20`; unknown avg `-0.0529` n `709`
- 4h: commodity avg `-0.0328` n `12`; crypto_alt avg `-0.7512` n `228`; crypto_major avg `-0.345` n `8`; equity avg `-0.0304` n `85`; fx avg `0.0082` n `6`; index avg `-0.0312` n `23`; metal avg `0.0891` n `20`; unknown avg `-0.3022` n `709`
- 24h: commodity avg `-0.9503` n `12`; crypto_alt avg `-0.7135` n `228`; crypto_major avg `-0.4036` n `8`; equity avg `-0.6234` n `85`; fx avg `0.1105` n `6`; index avg `0.0876` n `23`; metal avg `0.3064` n `18`; unknown avg `0.7068` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
