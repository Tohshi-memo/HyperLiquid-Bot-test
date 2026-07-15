# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T17:22:27.689907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0237` n `12`; crypto_alt avg `-0.0509` n `230`; crypto_major avg `-0.0037` n `8`; equity avg `0.234` n `94`; fx avg `-0.0009` n `6`; index avg `0.0347` n `25`; metal avg `0.0207` n `20`; unknown avg `-0.0108` n `768`
- 1h: commodity avg `0.0592` n `12`; crypto_alt avg `0.038` n `230`; crypto_major avg `0.036` n `8`; equity avg `0.8261` n `94`; fx avg `0.0321` n `6`; index avg `0.1153` n `25`; metal avg `0.0148` n `20`; unknown avg `0.0001` n `768`
- 4h: commodity avg `-0.0408` n `12`; crypto_alt avg `-1.1626` n `230`; crypto_major avg `-1.0751` n `8`; equity avg `-2.0405` n `93`; fx avg `0.1197` n `6`; index avg `-0.3792` n `25`; metal avg `-0.3424` n `20`; unknown avg `0.3004` n `768`
- 24h: commodity avg `0.1102` n `12`; crypto_alt avg `0.279` n `230`; crypto_major avg `1.3228` n `8`; equity avg `-1.1355` n `92`; fx avg `0.2052` n `6`; index avg `-0.2961` n `25`; metal avg `-0.2399` n `20`; unknown avg `0.3222` n `746`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
