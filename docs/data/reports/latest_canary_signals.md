# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T13:52:39.258372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2693` n `12`; crypto_alt avg `0.2857` n `228`; crypto_major avg `0.4585` n `8`; equity avg `0.7568` n `74`; fx avg `-0.0177` n `6`; index avg `0.3617` n `23`; metal avg `0.3031` n `18`; unknown avg `0.3853` n `556`
- 1h: commodity avg `-0.4992` n `12`; crypto_alt avg `0.4492` n `228`; crypto_major avg `0.4871` n `8`; equity avg `0.6014` n `74`; fx avg `-0.0259` n `6`; index avg `0.2773` n `23`; metal avg `0.6448` n `18`; unknown avg `0.2142` n `556`
- 4h: commodity avg `-0.0664` n `12`; crypto_alt avg `0.091` n `228`; crypto_major avg `0.336` n `8`; equity avg `0.2155` n `74`; fx avg `-0.0216` n `6`; index avg `0.1163` n `23`; metal avg `0.3153` n `18`; unknown avg `-1.209` n `556`
- 24h: commodity avg `-0.5515` n `12`; crypto_alt avg `0.1695` n `228`; crypto_major avg `0.2769` n `8`; equity avg `-0.8692` n `74`; fx avg `-0.0323` n `6`; index avg `-0.4691` n `23`; metal avg `-1.2383` n `18`; unknown avg `2.4989` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
