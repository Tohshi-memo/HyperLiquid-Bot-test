# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T02:22:30.831432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `12`; crypto_alt avg `0.0452` n `228`; crypto_major avg `0.011` n `8`; equity avg `0.0131` n `79`; fx avg `0.008` n `6`; index avg `-0.031` n `23`; metal avg `-0.0704` n `18`; unknown avg `0.2356` n `701`
- 1h: commodity avg `-0.0824` n `12`; crypto_alt avg `0.3338` n `228`; crypto_major avg `0.3318` n `8`; equity avg `0.2681` n `79`; fx avg `0.0363` n `6`; index avg `-0.0333` n `23`; metal avg `-0.3342` n `18`; unknown avg `0.1797` n `693`
- 4h: commodity avg `-0.4567` n `12`; crypto_alt avg `1.0741` n `228`; crypto_major avg `1.0178` n `8`; equity avg `-0.0294` n `79`; fx avg `0.1494` n `6`; index avg `0.1018` n `23`; metal avg `0.4054` n `18`; unknown avg `0.6184` n `685`
- 24h: commodity avg `-0.2962` n `12`; crypto_alt avg `0.6438` n `228`; crypto_major avg `-0.0996` n `8`; equity avg `-0.1927` n `79`; fx avg `0.1212` n `6`; index avg `0.0063` n `23`; metal avg `0.2419` n `18`; unknown avg `0.6958` n `629`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
