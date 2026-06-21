# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T18:22:26.283899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0212` n `12`; crypto_alt avg `0.0947` n `228`; crypto_major avg `0.0859` n `8`; equity avg `-0.0003` n `78`; fx avg `-0.0088` n `6`; index avg `-0.0139` n `23`; metal avg `0.0034` n `18`; unknown avg `-0.0291` n `702`
- 1h: commodity avg `0.0328` n `12`; crypto_alt avg `-0.3318` n `228`; crypto_major avg `-0.2442` n `8`; equity avg `-0.0554` n `78`; fx avg `0.007` n `6`; index avg `-0.0228` n `23`; metal avg `-0.077` n `18`; unknown avg `-0.2932` n `702`
- 4h: commodity avg `0.1705` n `12`; crypto_alt avg `-0.0191` n `228`; crypto_major avg `0.1039` n `8`; equity avg `-0.0241` n `78`; fx avg `-0.0969` n `6`; index avg `-0.0422` n `23`; metal avg `-0.0768` n `18`; unknown avg `-0.7942` n `702`
- 24h: commodity avg `0.1848` n `12`; crypto_alt avg `1.2998` n `228`; crypto_major avg `0.1706` n `8`; equity avg `0.3919` n `78`; fx avg `-0.069` n `6`; index avg `0.0013` n `23`; metal avg `-0.0906` n `18`; unknown avg `-0.4178` n `653`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
