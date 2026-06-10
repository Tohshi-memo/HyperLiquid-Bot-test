# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T08:07:35.393538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.022` n `12`; crypto_alt avg `-0.3471` n `228`; crypto_major avg `-0.4284` n `8`; equity avg `-0.1748` n `74`; fx avg `-0.0052` n `6`; index avg `-0.0905` n `23`; metal avg `-0.34` n `18`; unknown avg `0.0475` n `547`
- 1h: commodity avg `-0.0421` n `12`; crypto_alt avg `-0.1396` n `228`; crypto_major avg `0.0107` n `8`; equity avg `-0.2577` n `74`; fx avg `0.0032` n `6`; index avg `-0.1737` n `23`; metal avg `-0.6453` n `18`; unknown avg `0.0853` n `547`
- 4h: commodity avg `0.0808` n `12`; crypto_alt avg `-0.0432` n `228`; crypto_major avg `-0.2555` n `8`; equity avg `-0.0863` n `74`; fx avg `0.0518` n `6`; index avg `-0.3265` n `23`; metal avg `-0.1168` n `18`; unknown avg `-0.2718` n `537`
- 24h: commodity avg `-0.6353` n `12`; crypto_alt avg `-1.2328` n `228`; crypto_major avg `-3.3906` n `8`; equity avg `-3.5978` n `74`; fx avg `0.1443` n `6`; index avg `-1.8594` n `23`; metal avg `-3.2023` n `18`; unknown avg `-0.025` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
