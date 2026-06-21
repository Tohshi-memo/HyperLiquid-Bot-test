# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T06:52:25.247311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0412` n `12`; crypto_alt avg `-0.1115` n `228`; crypto_major avg `-0.0978` n `8`; equity avg `0.0204` n `78`; fx avg `0.0` n `6`; index avg `0.0176` n `23`; metal avg `-0.001` n `18`; unknown avg `0.0071` n `702`
- 1h: commodity avg `-0.0549` n `12`; crypto_alt avg `0.2308` n `228`; crypto_major avg `0.1037` n `8`; equity avg `0.093` n `78`; fx avg `0.0031` n `6`; index avg `0.0066` n `23`; metal avg `0.0582` n `18`; unknown avg `-0.3556` n `670`
- 4h: commodity avg `-0.0265` n `12`; crypto_alt avg `-0.0153` n `228`; crypto_major avg `-0.1682` n `8`; equity avg `0.2421` n `78`; fx avg `-0.0013` n `6`; index avg `0.0275` n `23`; metal avg `0.0682` n `18`; unknown avg `0.0472` n `662`
- 24h: commodity avg `0.0689` n `12`; crypto_alt avg `0.7974` n `228`; crypto_major avg `-0.0079` n `8`; equity avg `0.2029` n `78`; fx avg `0.0553` n `6`; index avg `-0.0018` n `23`; metal avg `0.0176` n `18`; unknown avg `-0.3209` n `533`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
