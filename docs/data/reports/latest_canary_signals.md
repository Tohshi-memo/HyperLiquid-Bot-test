# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T15:22:28.634882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `-0.0295` n `234`; crypto_major avg `-0.0598` n `8`; equity avg `-0.031` n `138`; fx avg `-0.0009` n `6`; index avg `0.0086` n `26`; metal avg `0.0264` n `20`; unknown avg `0.0722` n `919`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `-0.8376` n `234`; crypto_major avg `-0.7695` n `8`; equity avg `-0.0875` n `138`; fx avg `-0.0111` n `6`; index avg `-0.0174` n `26`; metal avg `-0.1019` n `20`; unknown avg `0.6707` n `915`
- 4h: commodity avg `0.0945` n `12`; crypto_alt avg `0.1963` n `234`; crypto_major avg `0.5177` n `8`; equity avg `0.4225` n `138`; fx avg `-0.0355` n `6`; index avg `0.1223` n `26`; metal avg `0.1823` n `20`; unknown avg `1.1091` n `891`
- 24h: commodity avg `-0.1113` n `12`; crypto_alt avg `4.0132` n `234`; crypto_major avg `2.1354` n `8`; equity avg `1.2024` n `138`; fx avg `0.0461` n `6`; index avg `0.167` n `26`; metal avg `0.1118` n `20`; unknown avg `0.4069` n `711`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
