# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T17:37:31.998209+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `-0.0619` n `228`; crypto_major avg `-0.1115` n `8`; equity avg `0.0043` n `74`; fx avg `0.0002` n `6`; index avg `-0.0013` n `23`; metal avg `0.0024` n `18`; unknown avg `-0.031` n `645`
- 1h: commodity avg `-0.0494` n `12`; crypto_alt avg `-0.1456` n `228`; crypto_major avg `-0.209` n `8`; equity avg `-0.0781` n `74`; fx avg `0.0082` n `6`; index avg `-0.0412` n `23`; metal avg `0.0149` n `18`; unknown avg `0.2508` n `645`
- 4h: commodity avg `-0.0325` n `12`; crypto_alt avg `-0.1314` n `228`; crypto_major avg `-0.4146` n `8`; equity avg `-0.0784` n `74`; fx avg `-0.0107` n `6`; index avg `0.0449` n `23`; metal avg `-0.0085` n `18`; unknown avg `0.2798` n `645`
- 24h: commodity avg `-0.1087` n `12`; crypto_alt avg `-1.4583` n `228`; crypto_major avg `-0.5312` n `8`; equity avg `0.4945` n `74`; fx avg `-0.0299` n `6`; index avg `0.233` n `23`; metal avg `-0.0165` n `18`; unknown avg `1.6789` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
