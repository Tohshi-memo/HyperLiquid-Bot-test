# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T12:52:27.544337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `12`; crypto_alt avg `0.1308` n `230`; crypto_major avg `0.1511` n `8`; equity avg `0.0998` n `102`; fx avg `0.0251` n `6`; index avg `0.0081` n `25`; metal avg `-0.0023` n `20`; unknown avg `0.0668` n `780`
- 1h: commodity avg `-0.0637` n `12`; crypto_alt avg `0.1567` n `230`; crypto_major avg `0.1062` n `8`; equity avg `-0.5467` n `102`; fx avg `0.0358` n `6`; index avg `-0.0761` n `25`; metal avg `0.0148` n `20`; unknown avg `0.2387` n `780`
- 4h: commodity avg `0.4938` n `12`; crypto_alt avg `-0.2899` n `230`; crypto_major avg `-0.152` n `8`; equity avg `-0.4842` n `102`; fx avg `0.087` n `6`; index avg `-0.082` n `25`; metal avg `-0.083` n `20`; unknown avg `1.0717` n `780`
- 24h: commodity avg `0.3945` n `12`; crypto_alt avg `-0.4174` n `230`; crypto_major avg `-0.241` n `8`; equity avg `5.3383` n `102`; fx avg `-0.0592` n `6`; index avg `0.795` n `25`; metal avg `0.06` n `20`; unknown avg `1.2636` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
