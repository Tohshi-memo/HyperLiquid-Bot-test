# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T05:37:20.029758+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.3` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.051` n `12`; crypto_alt avg `-0.3085` n `228`; crypto_major avg `-0.3292` n `8`; equity avg `-0.0367` n `72`; fx avg `0.0193` n `6`; index avg `-0.093` n `23`; metal avg `-0.2011` n `18`; unknown avg `0.7764` n `420`
- 1h: commodity avg `-0.0406` n `12`; crypto_alt avg `1.3801` n `228`; crypto_major avg `1.0488` n `8`; equity avg `0.0922` n `72`; fx avg `0.0307` n `6`; index avg `-0.0973` n `23`; metal avg `-0.1696` n `18`; unknown avg `1.0372` n `420`
- 4h: commodity avg `-0.0253` n `12`; crypto_alt avg `1.394` n `228`; crypto_major avg `0.8646` n `8`; equity avg `0.2637` n `72`; fx avg `0.0624` n `6`; index avg `-0.0254` n `23`; metal avg `0.0144` n `18`; unknown avg `0.8663` n `419`
- 24h: commodity avg `1.0396` n `12`; crypto_alt avg `-2.3584` n `228`; crypto_major avg `-4.4007` n `8`; equity avg `0.8671` n `72`; fx avg `0.0777` n `6`; index avg `1.1365` n `23`; metal avg `-1.2716` n `18`; unknown avg `-0.7726` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
