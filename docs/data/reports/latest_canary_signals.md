# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T13:22:31.466720+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0944` n `12`; crypto_alt avg `-0.1724` n `228`; crypto_major avg `-0.0179` n `8`; equity avg `0.0879` n `74`; fx avg `-0.0104` n `6`; index avg `0.045` n `23`; metal avg `0.1663` n `18`; unknown avg `0.0434` n `643`
- 1h: commodity avg `0.1035` n `12`; crypto_alt avg `-0.3617` n `228`; crypto_major avg `-0.1131` n `8`; equity avg `-0.4254` n `74`; fx avg `-0.0152` n `6`; index avg `-0.1499` n `23`; metal avg `-0.0356` n `18`; unknown avg `-0.1358` n `643`
- 4h: commodity avg `0.6626` n `12`; crypto_alt avg `-0.2379` n `228`; crypto_major avg `0.0714` n `8`; equity avg `-0.5453` n `74`; fx avg `0.0061` n `6`; index avg `-0.1404` n `23`; metal avg `-0.4851` n `18`; unknown avg `1.5124` n `643`
- 24h: commodity avg `-2.532` n `12`; crypto_alt avg `1.8442` n `228`; crypto_major avg `2.1554` n `8`; equity avg `2.6554` n `74`; fx avg `0.0049` n `6`; index avg `1.5935` n `23`; metal avg `2.949` n `18`; unknown avg `1.5838` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
