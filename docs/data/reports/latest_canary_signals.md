# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T15:52:19.258461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1791` n `12`; crypto_alt avg `-0.0887` n `228`; crypto_major avg `-0.1673` n `8`; equity avg `-0.1407` n `67`; fx avg `0.0108` n `6`; index avg `-0.001` n `23`; metal avg `0.0548` n `18`; unknown avg `0.1797` n `418`
- 1h: commodity avg `-0.0447` n `12`; crypto_alt avg `-1.0273` n `228`; crypto_major avg `-1.0393` n `8`; equity avg `-0.4369` n `67`; fx avg `0.0028` n `6`; index avg `-0.1889` n `23`; metal avg `-0.247` n `18`; unknown avg `-0.0896` n `418`
- 4h: commodity avg `0.6901` n `12`; crypto_alt avg `-0.8467` n `228`; crypto_major avg `-0.7023` n `8`; equity avg `-0.2326` n `67`; fx avg `-0.0206` n `6`; index avg `0.1967` n `23`; metal avg `-0.2556` n `18`; unknown avg `0.0262` n `415`
- 24h: commodity avg `1.0061` n `12`; crypto_alt avg `-1.079` n `228`; crypto_major avg `-1.1994` n `8`; equity avg `-0.6157` n `67`; fx avg `-0.1498` n `6`; index avg `0.1747` n `23`; metal avg `-1.2237` n `18`; unknown avg `-0.5377` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
