# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T07:22:24.364835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0129` n `12`; crypto_alt avg `-0.09` n `230`; crypto_major avg `-0.0574` n `8`; equity avg `-0.082` n `94`; fx avg `-0.0137` n `6`; index avg `-0.0088` n `25`; metal avg `-0.0402` n `20`; unknown avg `0.0075` n `768`
- 1h: commodity avg `-0.0704` n `12`; crypto_alt avg `-0.1502` n `230`; crypto_major avg `-0.1152` n `8`; equity avg `-0.2317` n `94`; fx avg `-0.0661` n `6`; index avg `-0.0366` n `25`; metal avg `-0.0868` n `20`; unknown avg `0.0262` n `768`
- 4h: commodity avg `-0.1066` n `12`; crypto_alt avg `-0.2274` n `230`; crypto_major avg `0.1037` n `8`; equity avg `-0.4334` n `94`; fx avg `-0.0762` n `6`; index avg `-0.0374` n `25`; metal avg `-0.0803` n `20`; unknown avg `-0.1232` n `752`
- 24h: commodity avg `-0.2209` n `12`; crypto_alt avg `0.2654` n `230`; crypto_major avg `0.3663` n `8`; equity avg `-2.4776` n `93`; fx avg `0.0427` n `6`; index avg `-0.4497` n `25`; metal avg `-0.0918` n `20`; unknown avg `-0.0782` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
