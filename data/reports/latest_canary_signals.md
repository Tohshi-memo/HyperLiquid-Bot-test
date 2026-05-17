# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T22:52:12.213711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `-1.6549` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0422` n `12`; crypto_alt avg `-0.1821` n `228`; crypto_major avg `-0.3673` n `8`; equity avg `0.0505` n `66`; fx avg `0.0004` n `5`; index avg `0.0039` n `23`; metal avg `0.1162` n `18`; unknown avg `-0.0254` n `383`
- 1h: commodity avg `0.1721` n `12`; crypto_alt avg `-0.9609` n `228`; crypto_major avg `-0.9298` n `8`; equity avg `0.2766` n `66`; fx avg `0.0104` n `5`; index avg `-0.0394` n `23`; metal avg `0.7251` n `18`; unknown avg `0.2513` n `383`
- 4h: commodity avg `-0.0133` n `12`; crypto_alt avg `-0.2163` n `228`; crypto_major avg `0.1148` n `8`; equity avg `0.6809` n `66`; fx avg `-0.02` n `5`; index avg `0.1421` n `23`; metal avg `0.681` n `18`; unknown avg `0.141` n `383`
- 24h: commodity avg `1.8612` n `12`; crypto_alt avg `-9.7395` n `228`; crypto_major avg `-2.0273` n `8`; equity avg `-2.1584` n `65`; fx avg `-0.1736` n `5`; index avg `-1.4586` n `23`; metal avg `-5.2705` n `18`; unknown avg `550.4701` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
