# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T23:37:25.115617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0374` n `12`; crypto_alt avg `0.2223` n `228`; crypto_major avg `0.1744` n `8`; equity avg `0.1063` n `78`; fx avg `0.0015` n `6`; index avg `0.0372` n `23`; metal avg `0.0172` n `18`; unknown avg `-0.1542` n `687`
- 1h: commodity avg `-0.1433` n `12`; crypto_alt avg `0.2162` n `228`; crypto_major avg `0.1259` n `8`; equity avg `0.2145` n `78`; fx avg `0.0091` n `6`; index avg `0.0491` n `23`; metal avg `0.0149` n `18`; unknown avg `-0.245` n `687`
- 4h: commodity avg `0.0109` n `12`; crypto_alt avg `0.5892` n `228`; crypto_major avg `0.3497` n `8`; equity avg `0.2713` n `78`; fx avg `0.0231` n `6`; index avg `0.0288` n `23`; metal avg `0.1344` n `18`; unknown avg `-0.6754` n `687`
- 24h: commodity avg `0.3123` n `12`; crypto_alt avg `-3.4798` n `228`; crypto_major avg `-4.4044` n `8`; equity avg `0.9345` n `78`; fx avg `-0.1139` n `6`; index avg `0.2596` n `23`; metal avg `-4.0945` n `18`; unknown avg `-0.7128` n `572`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
