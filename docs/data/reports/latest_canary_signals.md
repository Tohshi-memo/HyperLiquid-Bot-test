# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T09:07:27.793475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.0833` n `228`; crypto_major avg `-0.3849` n `8`; equity avg `-0.0437` n `86`; fx avg `-0.0091` n `6`; index avg `-0.0054` n `23`; metal avg `0.042` n `20`; unknown avg `-0.0162` n `765`
- 1h: commodity avg `-0.0746` n `12`; crypto_alt avg `-0.4677` n `228`; crypto_major avg `-0.7718` n `8`; equity avg `-0.4146` n `86`; fx avg `0.0219` n `6`; index avg `-0.0674` n `23`; metal avg `0.1078` n `20`; unknown avg `-0.0144` n `765`
- 4h: commodity avg `-0.117` n `12`; crypto_alt avg `0.9924` n `228`; crypto_major avg `0.8171` n `8`; equity avg `0.356` n `86`; fx avg `-0.0417` n `6`; index avg `0.1178` n `23`; metal avg `0.6561` n `20`; unknown avg `0.2047` n `733`
- 24h: commodity avg `0.0379` n `12`; crypto_alt avg `-1.8027` n `228`; crypto_major avg `-1.9937` n `8`; equity avg `-4.0668` n `86`; fx avg `0.0246` n `6`; index avg `-0.5972` n `23`; metal avg `0.422` n `20`; unknown avg `0.3931` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2507`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
