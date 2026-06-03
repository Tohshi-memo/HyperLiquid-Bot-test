# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T09:52:23.847515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.2217` n `12`; crypto_alt avg `0.3584` n `228`; crypto_major avg `0.3421` n `8`; equity avg `-0.0652` n `72`; fx avg `0.0173` n `6`; index avg `-0.0092` n `23`; metal avg `-0.0228` n `18`; unknown avg `0.0896` n `420`
- 1h: commodity avg `0.3237` n `12`; crypto_alt avg `0.0044` n `228`; crypto_major avg `0.1375` n `8`; equity avg `-0.2415` n `72`; fx avg `0.0433` n `6`; index avg `0.0188` n `23`; metal avg `-0.0133` n `18`; unknown avg `-0.4637` n `420`
- 4h: commodity avg `0.9244` n `12`; crypto_alt avg `0.6615` n `228`; crypto_major avg `0.3064` n `8`; equity avg `-0.2105` n `72`; fx avg `0.0267` n `6`; index avg `0.0101` n `23`; metal avg `-0.4236` n `18`; unknown avg `0.5601` n `410`
- 24h: commodity avg `2.0545` n `12`; crypto_alt avg `-0.5113` n `228`; crypto_major avg `-2.6327` n `8`; equity avg `0.3324` n `72`; fx avg `0.0664` n `6`; index avg `0.8282` n `23`; metal avg `-1.6732` n `18`; unknown avg `0.7446` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0416`, n `668`, weak_sample_signal
