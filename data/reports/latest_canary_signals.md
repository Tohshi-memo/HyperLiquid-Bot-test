# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T13:22:28.955726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `12`; crypto_alt avg `0.177` n `228`; crypto_major avg `0.0399` n `8`; equity avg `-0.015` n `74`; fx avg `-0.0211` n `6`; index avg `-0.0289` n `23`; metal avg `0.0725` n `18`; unknown avg `-0.0064` n `556`
- 1h: commodity avg `0.0992` n `12`; crypto_alt avg `0.4281` n `228`; crypto_major avg `0.173` n `8`; equity avg `-0.0964` n `74`; fx avg `-0.0061` n `6`; index avg `-0.059` n `23`; metal avg `0.3924` n `18`; unknown avg `0.1183` n `556`
- 4h: commodity avg `0.6268` n `12`; crypto_alt avg `0.1343` n `228`; crypto_major avg `0.1292` n `8`; equity avg `-0.3064` n `74`; fx avg `-0.0393` n `6`; index avg `-0.1646` n `23`; metal avg `-0.0997` n `18`; unknown avg `-1.2247` n `556`
- 24h: commodity avg `0.0692` n `12`; crypto_alt avg `0.9374` n `228`; crypto_major avg `0.9508` n `8`; equity avg `0.0658` n `74`; fx avg `-0.005` n `6`; index avg `-0.0954` n `23`; metal avg `-0.6265` n `18`; unknown avg `4.343` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
