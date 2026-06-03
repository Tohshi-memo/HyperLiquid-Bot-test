# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T18:52:24.614247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `0.466` n `228`; crypto_major avg `0.377` n `8`; equity avg `-0.065` n `73`; fx avg `-0.028` n `6`; index avg `-0.0433` n `23`; metal avg `0.0541` n `18`; unknown avg `-0.0064` n `419`
- 1h: commodity avg `0.0076` n `12`; crypto_alt avg `0.0692` n `228`; crypto_major avg `0.1518` n `8`; equity avg `-0.0378` n `73`; fx avg `-0.0406` n `6`; index avg `-0.0025` n `23`; metal avg `-0.1038` n `18`; unknown avg `-0.1994` n `419`
- 4h: commodity avg `0.269` n `12`; crypto_alt avg `-0.9116` n `228`; crypto_major avg `-0.5886` n `8`; equity avg `-0.775` n `73`; fx avg `-0.0384` n `6`; index avg `-0.2506` n `23`; metal avg `-0.7013` n `18`; unknown avg `-0.2021` n `419`
- 24h: commodity avg `0.795` n `12`; crypto_alt avg `1.4276` n `228`; crypto_major avg `-1.4827` n `8`; equity avg `-1.7142` n `72`; fx avg `0.0041` n `6`; index avg `-0.1734` n `23`; metal avg `-1.9898` n `18`; unknown avg `0.1832` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
