# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T04:22:27.528802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- risk_on_context: score `70.0` - Risk-on score is high; shorts need stricter confirmation.

## Class Returns

- 15m: commodity avg `0.0154` n `12`; crypto_alt avg `-0.0605` n `228`; crypto_major avg `0.0615` n `8`; equity avg `-0.0684` n `79`; fx avg `0.0048` n `6`; index avg `-0.0276` n `23`; metal avg `-0.0435` n `18`; unknown avg `-0.0902` n `701`
- 1h: commodity avg `-0.0669` n `12`; crypto_alt avg `-0.3626` n `228`; crypto_major avg `-0.5562` n `8`; equity avg `-0.1228` n `79`; fx avg `-0.0204` n `6`; index avg `-0.0561` n `23`; metal avg `-0.0326` n `18`; unknown avg `0.5288` n `701`
- 4h: commodity avg `-0.3909` n `12`; crypto_alt avg `0.5587` n `228`; crypto_major avg `0.2576` n `8`; equity avg `0.4687` n `79`; fx avg `0.0946` n `6`; index avg `0.1505` n `23`; metal avg `0.0851` n `18`; unknown avg `0.4929` n `685`
- 24h: commodity avg `-0.3437` n `12`; crypto_alt avg `-0.1511` n `228`; crypto_major avg `-1.2032` n `8`; equity avg `-0.5837` n `79`; fx avg `0.0054` n `6`; index avg `-0.0341` n `23`; metal avg `0.0863` n `18`; unknown avg `-0.2578` n `629`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
