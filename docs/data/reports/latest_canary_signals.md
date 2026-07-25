# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T00:52:24.873928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1009` n `12`; crypto_alt avg `-0.1067` n `230`; crypto_major avg `-0.1379` n `8`; equity avg `-0.0275` n `100`; fx avg `0.003` n `6`; index avg `-0.0054` n `25`; metal avg `-0.0035` n `20`; unknown avg `0.1407` n `774`
- 1h: commodity avg `0.0346` n `12`; crypto_alt avg `0.0326` n `230`; crypto_major avg `-0.0607` n `8`; equity avg `0.117` n `100`; fx avg `-0.0088` n `6`; index avg `0.0342` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.0109` n `774`
- 4h: commodity avg `-0.0267` n `12`; crypto_alt avg `-0.0144` n `230`; crypto_major avg `-0.0559` n `8`; equity avg `-0.1143` n `100`; fx avg `0.0305` n `6`; index avg `0.0142` n `25`; metal avg `0.0112` n `20`; unknown avg `-0.2593` n `774`
- 24h: commodity avg `-0.2994` n `12`; crypto_alt avg `-0.5905` n `230`; crypto_major avg `-0.6823` n `8`; equity avg `-2.9824` n `100`; fx avg `-0.0853` n `6`; index avg `-0.3521` n `25`; metal avg `0.0048` n `20`; unknown avg `13.9976` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1254`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1173`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1096`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1077`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
