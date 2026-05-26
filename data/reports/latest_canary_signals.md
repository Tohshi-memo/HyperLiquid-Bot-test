# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T09:22:20.706707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0648` n `12`; crypto_alt avg `0.1955` n `228`; crypto_major avg `0.1032` n `8`; equity avg `0.0093` n `67`; fx avg `0.0225` n `6`; index avg `0.0122` n `23`; metal avg `0.061` n `18`; unknown avg `0.1926` n `417`
- 1h: commodity avg `0.0697` n `12`; crypto_alt avg `0.0768` n `228`; crypto_major avg `0.0072` n `8`; equity avg `0.2028` n `67`; fx avg `0.0131` n `6`; index avg `0.0869` n `23`; metal avg `-0.0775` n `18`; unknown avg `-0.0888` n `417`
- 4h: commodity avg `0.5281` n `12`; crypto_alt avg `0.0442` n `228`; crypto_major avg `-0.2642` n `8`; equity avg `0.179` n `67`; fx avg `0.0048` n `6`; index avg `0.0173` n `23`; metal avg `-0.206` n `18`; unknown avg `-0.0376` n `397`
- 24h: commodity avg `0.9353` n `12`; crypto_alt avg `-0.57` n `228`; crypto_major avg `-1.5727` n `8`; equity avg `-0.4986` n `67`; fx avg `-0.094` n `6`; index avg `-0.0633` n `23`; metal avg `-0.5695` n `18`; unknown avg `-0.2323` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
