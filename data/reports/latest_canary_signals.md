# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T15:22:26.286861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0221` n `12`; crypto_alt avg `-0.1477` n `228`; crypto_major avg `-0.0754` n `8`; equity avg `0.0093` n `78`; fx avg `-0.0031` n `6`; index avg `0.0038` n `23`; metal avg `0.001` n `18`; unknown avg `0.0175` n `702`
- 1h: commodity avg `0.0067` n `12`; crypto_alt avg `0.2055` n `228`; crypto_major avg `0.3957` n `8`; equity avg `0.0491` n `78`; fx avg `-0.0066` n `6`; index avg `0.0012` n `23`; metal avg `0.0135` n `18`; unknown avg `0.1663` n `702`
- 4h: commodity avg `0.1422` n `12`; crypto_alt avg `0.2983` n `228`; crypto_major avg `0.331` n `8`; equity avg `0.0066` n `78`; fx avg `0.0319` n `6`; index avg `-0.0123` n `23`; metal avg `0.0049` n `18`; unknown avg `0.2904` n `702`
- 24h: commodity avg `0.0336` n `12`; crypto_alt avg `1.1235` n `228`; crypto_major avg `-0.2841` n `8`; equity avg `0.2395` n `78`; fx avg `0.0588` n `6`; index avg `0.0294` n `23`; metal avg `-0.1208` n `18`; unknown avg `0.6898` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
