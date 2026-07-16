# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T06:37:29.715434+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0407` n `12`; crypto_alt avg `-0.1561` n `230`; crypto_major avg `-0.2213` n `8`; equity avg `-0.1671` n `94`; fx avg `-0.021` n `6`; index avg `-0.0373` n `25`; metal avg `-0.0938` n `20`; unknown avg `-0.0179` n `768`
- 1h: commodity avg `-0.017` n `12`; crypto_alt avg `-0.2663` n `230`; crypto_major avg `-0.3234` n `8`; equity avg `-0.2664` n `94`; fx avg `-0.0099` n `6`; index avg `-0.0262` n `25`; metal avg `-0.105` n `20`; unknown avg `-0.0162` n `752`
- 4h: commodity avg `-0.1308` n `12`; crypto_alt avg `-0.3149` n `230`; crypto_major avg `-0.0076` n `8`; equity avg `-0.2124` n `94`; fx avg `-0.0391` n `6`; index avg `-0.037` n `25`; metal avg `-0.0791` n `20`; unknown avg `-0.2091` n `752`
- 24h: commodity avg `-0.0846` n `12`; crypto_alt avg `-0.2494` n `230`; crypto_major avg `-0.317` n `8`; equity avg `-2.4879` n `93`; fx avg `0.1129` n `6`; index avg `-0.4763` n `25`; metal avg `-0.0618` n `20`; unknown avg `-0.1794` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
