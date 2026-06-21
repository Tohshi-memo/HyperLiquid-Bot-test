# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T08:07:29.944144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `0.1366` n `228`; crypto_major avg `-0.1575` n `8`; equity avg `-0.0162` n `78`; fx avg `-0.0037` n `6`; index avg `0.0063` n `23`; metal avg `0.018` n `18`; unknown avg `-0.0132` n `702`
- 1h: commodity avg `-0.0111` n `12`; crypto_alt avg `0.2611` n `228`; crypto_major avg `-0.2323` n `8`; equity avg `-0.0216` n `78`; fx avg `-0.0045` n `6`; index avg `0.0001` n `23`; metal avg `-0.0187` n `18`; unknown avg `0.2863` n `694`
- 4h: commodity avg `-0.0899` n `12`; crypto_alt avg `0.3808` n `228`; crypto_major avg `-0.4564` n `8`; equity avg `0.1226` n `78`; fx avg `0.098` n `6`; index avg `0.022` n `23`; metal avg `0.0418` n `18`; unknown avg `0.4867` n `654`
- 24h: commodity avg `0.0383` n `12`; crypto_alt avg `1.6203` n `228`; crypto_major avg `0.1311` n `8`; equity avg `0.2881` n `78`; fx avg `0.042` n `6`; index avg `0.0586` n `23`; metal avg `-0.0306` n `18`; unknown avg `0.2402` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0526`, n `668`, weak_sample_signal
