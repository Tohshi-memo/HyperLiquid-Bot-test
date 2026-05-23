# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T10:52:14.405006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `12`; crypto_alt avg `-0.1519` n `228`; crypto_major avg `-0.062` n `8`; equity avg `0.0344` n `67`; fx avg `0.0006` n `6`; index avg `-0.0029` n `23`; metal avg `0.0007` n `18`; unknown avg `0.0011` n `396`
- 1h: commodity avg `0.0028` n `12`; crypto_alt avg `0.0441` n `228`; crypto_major avg `0.0948` n `8`; equity avg `0.0395` n `67`; fx avg `0.0031` n `6`; index avg `-0.0932` n `23`; metal avg `-0.0726` n `18`; unknown avg `-0.3102` n `396`
- 4h: commodity avg `-0.0331` n `12`; crypto_alt avg `-1.3971` n `228`; crypto_major avg `-0.8672` n `8`; equity avg `-0.1183` n `67`; fx avg `-0.0247` n `6`; index avg `-0.1732` n `23`; metal avg `-0.1121` n `18`; unknown avg `-0.0315` n `386`
- 24h: commodity avg `-0.2635` n `12`; crypto_alt avg `-5.4666` n `228`; crypto_major avg `-3.7887` n `8`; equity avg `-1.4746` n `67`; fx avg `0.054` n `6`; index avg `-0.101` n `23`; metal avg `-0.7915` n `18`; unknown avg `-2.2175` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0463`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0437`, n `668`, weak_sample_signal
