# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T12:52:30.034713+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0263` n `12`; crypto_alt avg `0.0232` n `230`; crypto_major avg `0.1636` n `8`; equity avg `0.0211` n `96`; fx avg `-0.0007` n `6`; index avg `-0.0033` n `25`; metal avg `0.0064` n `20`; unknown avg `0.0267` n `770`
- 1h: commodity avg `0.0148` n `12`; crypto_alt avg `-0.0205` n `230`; crypto_major avg `0.1676` n `8`; equity avg `-0.0661` n `96`; fx avg `0.0001` n `6`; index avg `-0.0251` n `25`; metal avg `-0.0058` n `20`; unknown avg `0.0503` n `770`
- 4h: commodity avg `0.1487` n `12`; crypto_alt avg `-0.1148` n `230`; crypto_major avg `0.0934` n `8`; equity avg `-0.1255` n `96`; fx avg `-0.009` n `6`; index avg `-0.0223` n `25`; metal avg `-0.0083` n `20`; unknown avg `-0.0559` n `769`
- 24h: commodity avg `0.6684` n `12`; crypto_alt avg `-0.2467` n `230`; crypto_major avg `0.6986` n `8`; equity avg `1.1639` n `96`; fx avg `0.032` n `6`; index avg `0.2024` n `25`; metal avg `0.4078` n `20`; unknown avg `0.1135` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
