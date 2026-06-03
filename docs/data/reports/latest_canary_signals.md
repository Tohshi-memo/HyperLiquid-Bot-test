# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T15:22:37.424847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0618` n `12`; crypto_alt avg `-0.1263` n `228`; crypto_major avg `-0.1591` n `8`; equity avg `-0.1783` n `73`; fx avg `-0.0142` n `6`; index avg `-0.1275` n `23`; metal avg `-0.1836` n `18`; unknown avg `0.2493` n `419`
- 1h: commodity avg `0.2021` n `12`; crypto_alt avg `0.2774` n `228`; crypto_major avg `-0.0865` n `8`; equity avg `-0.377` n `73`; fx avg `-0.0038` n `6`; index avg `0.0153` n `23`; metal avg `-0.1892` n `18`; unknown avg `0.133` n `419`
- 4h: commodity avg `-0.5297` n `12`; crypto_alt avg `-0.3436` n `228`; crypto_major avg `-1.4378` n `8`; equity avg `-1.9409` n `73`; fx avg `-0.0522` n `6`; index avg `-0.5541` n `23`; metal avg `-0.9719` n `18`; unknown avg `0.0441` n `419`
- 24h: commodity avg `1.2672` n `12`; crypto_alt avg `1.8863` n `228`; crypto_major avg `-2.099` n `8`; equity avg `-1.453` n `72`; fx avg `0.0105` n `6`; index avg `-0.0819` n `23`; metal avg `-2.0905` n `18`; unknown avg `1.4089` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
