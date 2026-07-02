# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T07:22:32.298978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0326` n `12`; crypto_alt avg `-0.0525` n `228`; crypto_major avg `-0.128` n `8`; equity avg `-0.2151` n `88`; fx avg `0.0014` n `6`; index avg `-0.0316` n `25`; metal avg `-0.0928` n `20`; unknown avg `0.0308` n `763`
- 1h: commodity avg `-0.1183` n `12`; crypto_alt avg `-0.2272` n `228`; crypto_major avg `-0.5115` n `8`; equity avg `-0.5609` n `88`; fx avg `-0.0451` n `6`; index avg `-0.0884` n `25`; metal avg `-0.2382` n `20`; unknown avg `0.1671` n `763`
- 4h: commodity avg `-0.0346` n `12`; crypto_alt avg `-0.0517` n `228`; crypto_major avg `-0.1435` n `8`; equity avg `-1.4344` n `88`; fx avg `-0.0431` n `6`; index avg `-0.3118` n `25`; metal avg `-0.1224` n `20`; unknown avg `0.1956` n `739`
- 24h: commodity avg `-0.6401` n `12`; crypto_alt avg `1.9373` n `228`; crypto_major avg `1.193` n `8`; equity avg `-2.4576` n `88`; fx avg `-0.0388` n `6`; index avg `-0.5919` n `25`; metal avg `1.0831` n `20`; unknown avg `25.053` n `739`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
