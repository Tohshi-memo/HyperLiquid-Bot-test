# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T18:52:29.623020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0978` n `12`; crypto_alt avg `0.1117` n `228`; crypto_major avg `0.1185` n `8`; equity avg `0.045` n `74`; fx avg `-0.0171` n `6`; index avg `-0.0063` n `23`; metal avg `0.0037` n `18`; unknown avg `0.0122` n `645`
- 1h: commodity avg `0.2411` n `12`; crypto_alt avg `0.1101` n `228`; crypto_major avg `0.0585` n `8`; equity avg `0.0089` n `74`; fx avg `0.001` n `6`; index avg `-0.0324` n `23`; metal avg `0.1445` n `18`; unknown avg `-0.4066` n `645`
- 4h: commodity avg `0.1638` n `12`; crypto_alt avg `0.3259` n `228`; crypto_major avg `0.2686` n `8`; equity avg `0.1134` n `74`; fx avg `-0.0337` n `6`; index avg `0.0972` n `23`; metal avg `0.017` n `18`; unknown avg `-0.2941` n `645`
- 24h: commodity avg `0.1959` n `12`; crypto_alt avg `-1.2364` n `228`; crypto_major avg `-0.5262` n `8`; equity avg `0.315` n `74`; fx avg `-0.0704` n `6`; index avg `0.2043` n `23`; metal avg `-0.0813` n `18`; unknown avg `0.9322` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
