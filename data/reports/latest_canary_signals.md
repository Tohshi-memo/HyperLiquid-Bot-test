# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T05:37:31.035261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0333` n `12`; crypto_alt avg `-0.1411` n `230`; crypto_major avg `-0.1217` n `8`; equity avg `-0.1577` n `108`; fx avg `-0.0301` n `6`; index avg `-0.0286` n `25`; metal avg `-0.0037` n `20`; unknown avg `0.0251` n `782`
- 1h: commodity avg `0.045` n `12`; crypto_alt avg `-0.0268` n `230`; crypto_major avg `0.1702` n `8`; equity avg `-0.0139` n `108`; fx avg `-0.0391` n `6`; index avg `-0.0156` n `25`; metal avg `-0.047` n `20`; unknown avg `0.3501` n `782`
- 4h: commodity avg `-0.1656` n `12`; crypto_alt avg `0.0846` n `230`; crypto_major avg `0.0046` n `8`; equity avg `0.5705` n `108`; fx avg `-0.011` n `6`; index avg `0.0351` n `25`; metal avg `-0.184` n `20`; unknown avg `0.3009` n `782`
- 24h: commodity avg `0.001` n `12`; crypto_alt avg `-0.0398` n `230`; crypto_major avg `-0.0304` n `8`; equity avg `-2.0994` n `108`; fx avg `-0.0624` n `6`; index avg `-0.3851` n `25`; metal avg `0.3217` n `20`; unknown avg `0.8294` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
