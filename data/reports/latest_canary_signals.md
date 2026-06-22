# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T18:22:29.994356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0547` n `12`; crypto_alt avg `0.0962` n `228`; crypto_major avg `0.3851` n `8`; equity avg `0.1898` n `85`; fx avg `0.0024` n `6`; index avg `-0.0311` n `23`; metal avg `0.0678` n `20`; unknown avg `-0.0557` n `717`
- 1h: commodity avg `-0.09` n `12`; crypto_alt avg `0.2381` n `228`; crypto_major avg `0.8458` n `8`; equity avg `0.4263` n `85`; fx avg `0.0033` n `6`; index avg `-0.0222` n `23`; metal avg `0.0101` n `20`; unknown avg `-0.0231` n `717`
- 4h: commodity avg `-0.1014` n `12`; crypto_alt avg `-0.8386` n `228`; crypto_major avg `-0.3723` n `8`; equity avg `-0.3816` n `85`; fx avg `-0.0333` n `6`; index avg `-0.0988` n `23`; metal avg `-0.1164` n `20`; unknown avg `-0.264` n `716`
- 24h: commodity avg `-0.9765` n `12`; crypto_alt avg `-0.0035` n `228`; crypto_major avg `0.7467` n `8`; equity avg `-0.132` n `85`; fx avg `0.0447` n `6`; index avg `0.1361` n `23`; metal avg `0.319` n `18`; unknown avg `1.0144` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
