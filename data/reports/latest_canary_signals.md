# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T14:52:25.797589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0883` n `12`; crypto_alt avg `-0.0749` n `230`; crypto_major avg `0.0219` n `8`; equity avg `-0.1991` n `98`; fx avg `-0.0022` n `6`; index avg `-0.0665` n `25`; metal avg `0.0263` n `20`; unknown avg `-0.0678` n `770`
- 1h: commodity avg `0.0488` n `12`; crypto_alt avg `-0.0668` n `230`; crypto_major avg `-0.2335` n `8`; equity avg `-0.5487` n `98`; fx avg `-0.0082` n `6`; index avg `-0.1356` n `25`; metal avg `0.0189` n `20`; unknown avg `-0.0763` n `770`
- 4h: commodity avg `0.0012` n `12`; crypto_alt avg `0.0109` n `230`; crypto_major avg `-0.0271` n `8`; equity avg `-0.5937` n `98`; fx avg `-0.0656` n `6`; index avg `-0.0423` n `25`; metal avg `0.0091` n `20`; unknown avg `0.3086` n `770`
- 24h: commodity avg `-0.5355` n `12`; crypto_alt avg `0.2432` n `230`; crypto_major avg `-0.4007` n `8`; equity avg `-0.0043` n `97`; fx avg `-0.092` n `6`; index avg `0.0835` n `25`; metal avg `0.2152` n `20`; unknown avg `-0.079` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1091`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0966`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0871`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0791`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
