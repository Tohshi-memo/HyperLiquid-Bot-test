# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T01:22:10.753380+00:00`
- Correlation status: `ready`
- Asset price records: `601`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1038` n `12`; crypto_alt avg `-0.2058` n `228`; crypto_major avg `-0.143` n `8`; equity avg `0.1506` n `65`; fx avg `-0.0013` n `5`; index avg `0.034` n `23`; metal avg `0.0066` n `18`; unknown avg `0.015` n `365`
- 1h: commodity avg `-0.379` n `12`; crypto_alt avg `-0.4367` n `228`; crypto_major avg `-0.4603` n `8`; equity avg `0.3709` n `65`; fx avg `0.0142` n `5`; index avg `0.1676` n `23`; metal avg `0.5987` n `18`; unknown avg `0.0469` n `365`
- 4h: commodity avg `-0.9125` n `12`; crypto_alt avg `0.2654` n `228`; crypto_major avg `-0.3034` n `8`; equity avg `0.5202` n `65`; fx avg `0.0922` n `5`; index avg `0.3688` n `23`; metal avg `0.9042` n `18`; unknown avg `-0.2047` n `365`
- 24h: commodity avg `0.4733` n `12`; crypto_alt avg `2.166` n `228`; crypto_major avg `-1.4273` n `8`; equity avg `-0.4779` n `65`; fx avg `0.1959` n `5`; index avg `-0.4849` n `23`; metal avg `0.0653` n `18`; unknown avg `-0.1794` n `354`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1351`, n `597`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1141`, n `597`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1116`, n `597`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.107`, n `593`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1055`, n `597`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1052`, n `593`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0921`, n `593`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0903`, n `593`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.08`, n `593`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0719`, n `597`, weak_sample_signal
