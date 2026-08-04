# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T05:37:32.508883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `-0.0083` n `230`; crypto_major avg `-0.0413` n `8`; equity avg `0.4002` n `107`; fx avg `0.0038` n `6`; index avg `0.0937` n `25`; metal avg `0.0188` n `20`; unknown avg `-0.1175` n `781`
- 1h: commodity avg `0.0356` n `12`; crypto_alt avg `-0.1071` n `230`; crypto_major avg `-0.0847` n `8`; equity avg `0.4145` n `107`; fx avg `-0.0127` n `6`; index avg `0.0941` n `25`; metal avg `-0.0135` n `20`; unknown avg `0.0589` n `781`
- 4h: commodity avg `0.1357` n `12`; crypto_alt avg `0.0854` n `230`; crypto_major avg `0.2089` n `8`; equity avg `0.6881` n `107`; fx avg `0.0669` n `6`; index avg `0.1231` n `25`; metal avg `0.1454` n `20`; unknown avg `5.2476` n `780`
- 24h: commodity avg `0.4042` n `12`; crypto_alt avg `1.1267` n `230`; crypto_major avg `1.2583` n `8`; equity avg `2.0679` n `107`; fx avg `0.0405` n `6`; index avg `0.1977` n `25`; metal avg `0.0906` n `20`; unknown avg `0.1657` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
