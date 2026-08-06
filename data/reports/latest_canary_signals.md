# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T12:07:25.897597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0505` n `12`; crypto_alt avg `-0.1336` n `230`; crypto_major avg `-0.1501` n `8`; equity avg `-0.1078` n `109`; fx avg `-0.0024` n `6`; index avg `-0.0078` n `25`; metal avg `0.0216` n `20`; unknown avg `-0.0314` n `781`
- 1h: commodity avg `-0.0916` n `12`; crypto_alt avg `0.3145` n `230`; crypto_major avg `0.0945` n `8`; equity avg `0.3986` n `109`; fx avg `-0.0053` n `6`; index avg `0.034` n `25`; metal avg `-0.0169` n `20`; unknown avg `0.0674` n `781`
- 4h: commodity avg `-0.0522` n `12`; crypto_alt avg `-0.2727` n `230`; crypto_major avg `-0.4975` n `8`; equity avg `-0.111` n `109`; fx avg `-0.0458` n `6`; index avg `-0.0492` n `25`; metal avg `0.0903` n `20`; unknown avg `108.1042` n `781`
- 24h: commodity avg `-0.1398` n `12`; crypto_alt avg `0.1009` n `230`; crypto_major avg `-0.5134` n `8`; equity avg `-1.5807` n `109`; fx avg `-0.0068` n `6`; index avg `-0.3994` n `25`; metal avg `0.206` n `20`; unknown avg `113.1054` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
