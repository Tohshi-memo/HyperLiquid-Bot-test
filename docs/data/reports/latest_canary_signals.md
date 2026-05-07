# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T14:37:13.645470+00:00`
- Correlation status: `ready`
- Asset price records: `558`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.4146` n `12`; crypto_alt avg `-0.7475` n `228`; crypto_major avg `-0.4802` n `8`; equity avg `-0.1925` n `65`; fx avg `-0.014` n `5`; index avg `0.0843` n `23`; metal avg `0.0281` n `18`; unknown avg `-0.1834` n `365`
- 1h: commodity avg `0.2404` n `12`; crypto_alt avg `-1.1205` n `228`; crypto_major avg `-0.9377` n `8`; equity avg `-0.1273` n `65`; fx avg `-0.02` n `5`; index avg `0.0073` n `23`; metal avg `0.0169` n `18`; unknown avg `-0.4384` n `365`
- 4h: commodity avg `-0.791` n `12`; crypto_alt avg `-0.506` n `228`; crypto_major avg `-0.9375` n `8`; equity avg `-0.1155` n `65`; fx avg `-0.0359` n `5`; index avg `-0.2081` n `23`; metal avg `0.3573` n `18`; unknown avg `-0.1002` n `365`
- 24h: commodity avg `-1.1757` n `12`; crypto_alt avg `0.2319` n `228`; crypto_major avg `-1.9873` n `8`; equity avg `1.344` n `65`; fx avg `0.1003` n `5`; index avg `0.5824` n `23`; metal avg `1.7245` n `18`; unknown avg `-0.0095` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.136`, n `554`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1248`, n `554`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0995`, n `554`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0907`, n `554`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0879`, n `554`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `550`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0796`, n `550`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0761`, n `550`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.075`, n `550`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `554`, weak_sample_signal
