# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T16:22:30.228632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0668` n `12`; crypto_alt avg `-0.0594` n `228`; crypto_major avg `0.0617` n `8`; equity avg `0.0226` n `78`; fx avg `-0.0006` n `6`; index avg `-0.0114` n `23`; metal avg `-0.0021` n `18`; unknown avg `-0.3074` n `702`
- 1h: commodity avg `0.0436` n `12`; crypto_alt avg `0.204` n `228`; crypto_major avg `-0.0051` n `8`; equity avg `0.0095` n `78`; fx avg `0.0` n `6`; index avg `-0.0243` n `23`; metal avg `-0.0134` n `18`; unknown avg `-0.3448` n `702`
- 4h: commodity avg `-0.0209` n `12`; crypto_alt avg `0.742` n `228`; crypto_major avg `0.7422` n `8`; equity avg `0.0414` n `78`; fx avg `0.0525` n `6`; index avg `-0.0215` n `23`; metal avg `-0.0076` n `18`; unknown avg `-0.0175` n `702`
- 24h: commodity avg `0.0897` n `12`; crypto_alt avg `1.597` n `228`; crypto_major avg `0.0858` n `8`; equity avg `0.3235` n `78`; fx avg `0.0204` n `6`; index avg `0.002` n `23`; metal avg `-0.0979` n `18`; unknown avg `0.2642` n `653`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
