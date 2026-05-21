# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T11:22:20.218362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.68` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1991` n `12`; crypto_alt avg `0.2483` n `228`; crypto_major avg `0.0493` n `8`; equity avg `0.331` n `66`; fx avg `0.0104` n `6`; index avg `0.188` n `23`; metal avg `0.1643` n `18`; unknown avg `0.1404` n `386`
- 1h: commodity avg `0.8608` n `12`; crypto_alt avg `-0.6312` n `228`; crypto_major avg `-0.6472` n `8`; equity avg `-0.3574` n `66`; fx avg `0.0263` n `6`; index avg `-0.2635` n `23`; metal avg `-0.3961` n `18`; unknown avg `1.6545` n `386`
- 4h: commodity avg `0.0979` n `12`; crypto_alt avg `-0.3725` n `228`; crypto_major avg `-0.3537` n `8`; equity avg `0.2341` n `66`; fx avg `0.0751` n `6`; index avg `0.0078` n `23`; metal avg `0.1262` n `18`; unknown avg `2.5081` n `385`
- 24h: commodity avg `-1.3934` n `12`; crypto_alt avg `1.8094` n `228`; crypto_major avg `2.1144` n `8`; equity avg `1.1659` n `66`; fx avg `0.1052` n `6`; index avg `0.9888` n `23`; metal avg `-0.0896` n `18`; unknown avg `7.9706` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
