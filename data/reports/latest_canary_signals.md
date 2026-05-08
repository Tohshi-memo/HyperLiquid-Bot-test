# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T16:43:08.729636+00:00`
- Correlation status: `ready`
- Asset price records: `662`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3065` n `12`; crypto_alt avg `0.0785` n `228`; crypto_major avg `-0.0958` n `8`; equity avg `-0.1647` n `65`; fx avg `-0.0148` n `5`; index avg `0.0322` n `23`; metal avg `0.0275` n `18`; unknown avg `-0.015` n `375`
- 1h: commodity avg `0.1954` n `12`; crypto_alt avg `0.727` n `228`; crypto_major avg `0.2946` n `8`; equity avg `-0.1978` n `65`; fx avg `0.003` n `5`; index avg `0.0172` n `23`; metal avg `0.094` n `18`; unknown avg `-0.0336` n `375`
- 4h: commodity avg `0.5794` n `12`; crypto_alt avg `1.2253` n `228`; crypto_major avg `0.2295` n `8`; equity avg `0.7513` n `65`; fx avg `-0.0411` n `5`; index avg `0.3395` n `23`; metal avg `-0.4794` n `18`; unknown avg `0.1041` n `375`
- 24h: commodity avg `0.7861` n `12`; crypto_alt avg `2.8825` n `228`; crypto_major avg `0.3469` n `8`; equity avg `1.9226` n `65`; fx avg `0.1392` n `5`; index avg `0.8476` n `23`; metal avg `0.0558` n `18`; unknown avg `0.1225` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1207`, n `654`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1166`, n `658`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1164`, n `654`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1043`, n `654`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0999`, n `658`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0966`, n `654`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `658`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `658`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.073`, n `658`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `658`, weak_sample_signal
