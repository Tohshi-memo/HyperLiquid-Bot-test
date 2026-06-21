# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T04:37:27.439397+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `12`; crypto_alt avg `0.094` n `228`; crypto_major avg `-0.011` n `8`; equity avg `0.0166` n `78`; fx avg `0.0` n `6`; index avg `-0.0013` n `23`; metal avg `0.0002` n `18`; unknown avg `-0.1523` n `702`
- 1h: commodity avg `0.0105` n `12`; crypto_alt avg `0.095` n `228`; crypto_major avg `0.0255` n `8`; equity avg `0.0633` n `78`; fx avg `-0.0042` n `6`; index avg `0.005` n `23`; metal avg `-0.0078` n `18`; unknown avg `-0.116` n `702`
- 4h: commodity avg `0.0043` n `12`; crypto_alt avg `0.3145` n `228`; crypto_major avg `0.1634` n `8`; equity avg `0.2078` n `78`; fx avg `-0.0111` n `6`; index avg `0.0275` n `23`; metal avg `0.0276` n `18`; unknown avg `0.3734` n `701`
- 24h: commodity avg `0.2337` n `12`; crypto_alt avg `1.5386` n `228`; crypto_major avg `1.388` n `8`; equity avg `0.4007` n `78`; fx avg `0.0542` n `6`; index avg `-0.0021` n `23`; metal avg `-0.0234` n `18`; unknown avg `1.6243` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
