# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T14:52:26.962415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1053` n `12`; crypto_alt avg `0.1954` n `228`; crypto_major avg `-0.0109` n `8`; equity avg `0.1162` n `73`; fx avg `0.0221` n `6`; index avg `0.0254` n `23`; metal avg `0.0795` n `18`; unknown avg `-0.107` n `419`
- 1h: commodity avg `0.2039` n `12`; crypto_alt avg `0.107` n `228`; crypto_major avg `-0.2167` n `8`; equity avg `0.371` n `73`; fx avg `0.0072` n `6`; index avg `0.4183` n `23`; metal avg `0.1269` n `18`; unknown avg `0.0064` n `419`
- 4h: commodity avg `-0.6461` n `12`; crypto_alt avg `0.4256` n `228`; crypto_major avg `-0.7644` n `8`; equity avg `-1.2844` n `73`; fx avg `-0.0544` n `6`; index avg `-0.3645` n `23`; metal avg `-0.6258` n `18`; unknown avg `0.087` n `419`
- 24h: commodity avg `1.1451` n `12`; crypto_alt avg `1.0885` n `228`; crypto_major avg `-2.581` n `8`; equity avg `-0.9525` n `72`; fx avg `0.0001` n `6`; index avg `0.1647` n `23`; metal avg `-1.6351` n `18`; unknown avg `0.3651` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
