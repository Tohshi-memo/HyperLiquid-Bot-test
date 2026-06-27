# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T21:37:25.629140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1268` n `12`; crypto_alt avg `-0.2695` n `228`; crypto_major avg `-0.1337` n `8`; equity avg `0.0564` n `88`; fx avg `-0.0008` n `6`; index avg `-0.0001` n `23`; metal avg `0.0189` n `20`; unknown avg `-0.0274` n `764`
- 1h: commodity avg `0.0347` n `12`; crypto_alt avg `-0.1276` n `228`; crypto_major avg `0.092` n `8`; equity avg `0.0711` n `88`; fx avg `0.0044` n `6`; index avg `-0.0029` n `23`; metal avg `0.0202` n `20`; unknown avg `0.0627` n `764`
- 4h: commodity avg `0.0273` n `12`; crypto_alt avg `-0.7281` n `228`; crypto_major avg `-0.8016` n `8`; equity avg `0.055` n `88`; fx avg `0.0022` n `6`; index avg `0.0066` n `23`; metal avg `-0.0002` n `20`; unknown avg `-0.1726` n `764`
- 24h: commodity avg `0.0821` n `12`; crypto_alt avg `-0.483` n `228`; crypto_major avg `-0.3937` n `8`; equity avg `0.6001` n `88`; fx avg `-0.0324` n `6`; index avg `0.0254` n `23`; metal avg `0.0269` n `20`; unknown avg `-0.2342` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
