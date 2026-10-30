# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T16:22:35.879383+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `13`; crypto_alt avg `0.0038` n `238`; crypto_major avg `-0.0748` n `8`; equity avg `-0.0413` n `156`; fx avg `-0.0003` n `6`; index avg `0.0032` n `27`; metal avg `-0.0024` n `20`; unknown avg `0.0864` n `1261`
- 1h: commodity avg `0.0404` n `13`; crypto_alt avg `-0.6977` n `238`; crypto_major avg `-0.724` n `8`; equity avg `-0.6105` n `156`; fx avg `0.047` n `6`; index avg `-0.0559` n `27`; metal avg `-0.0502` n `20`; unknown avg `0.616` n `1249`
- 4h: commodity avg `0.1398` n `13`; crypto_alt avg `0.2462` n `238`; crypto_major avg `-0.3395` n `8`; equity avg `-1.3465` n `156`; fx avg `-0.039` n `6`; index avg `-0.0514` n `27`; metal avg `-0.1775` n `20`; unknown avg `4.4235` n `1149`
- 24h: commodity avg `0.6137` n `13`; crypto_alt avg `-5.7121` n `238`; crypto_major avg `-4.9334` n `8`; equity avg `-6.0948` n `156`; fx avg `-0.0851` n `6`; index avg `-0.4997` n `27`; metal avg `-0.9453` n `20`; unknown avg `52.0551` n `1038`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.168`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
