# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T06:07:29.638324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.016` n `12`; crypto_alt avg `0.1089` n `228`; crypto_major avg `0.0316` n `8`; equity avg `0.0352` n `78`; fx avg `0.0038` n `6`; index avg `-0.0043` n `23`; metal avg `0.02` n `18`; unknown avg `-0.3939` n `670`
- 1h: commodity avg `-0.0098` n `12`; crypto_alt avg `0.0163` n `228`; crypto_major avg `-0.0239` n `8`; equity avg `0.0393` n `78`; fx avg `-0.0011` n `6`; index avg `-0.0028` n `23`; metal avg `0.0241` n `18`; unknown avg `-0.4598` n `670`
- 4h: commodity avg `0.0169` n `12`; crypto_alt avg `-0.1975` n `228`; crypto_major avg `-0.3438` n `8`; equity avg `0.1786` n `78`; fx avg `-0.0019` n `6`; index avg `0.0234` n `23`; metal avg `0.0395` n `18`; unknown avg `0.0845` n `662`
- 24h: commodity avg `0.1497` n `12`; crypto_alt avg `0.7938` n `228`; crypto_major avg `0.073` n `8`; equity avg `0.2016` n `78`; fx avg `0.0684` n `6`; index avg `-0.0011` n `23`; metal avg `0.0011` n `18`; unknown avg `-0.3059` n `533`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
