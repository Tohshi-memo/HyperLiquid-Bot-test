# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T19:37:31.865466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0432` n `13`; crypto_alt avg `0.1878` n `238`; crypto_major avg `0.1301` n `8`; equity avg `0.2005` n `156`; fx avg `-0.0015` n `6`; index avg `0.0349` n `27`; metal avg `0.0381` n `20`; unknown avg `166.9197` n `1261`
- 1h: commodity avg `-0.0768` n `13`; crypto_alt avg `0.3352` n `238`; crypto_major avg `0.2484` n `8`; equity avg `0.926` n `156`; fx avg `0.008` n `6`; index avg `0.0922` n `27`; metal avg `0.0539` n `20`; unknown avg `15.1059` n `1255`
- 4h: commodity avg `-0.0044` n `13`; crypto_alt avg `-0.3936` n `238`; crypto_major avg `-0.6293` n `8`; equity avg `-0.7338` n `156`; fx avg `0.0357` n `6`; index avg `-0.093` n `27`; metal avg `-0.1285` n `20`; unknown avg `7.9147` n `1251`
- 24h: commodity avg `0.2988` n `13`; crypto_alt avg `-4.5833` n `238`; crypto_major avg `-4.2688` n `8`; equity avg `-5.7401` n `156`; fx avg `-0.0891` n `6`; index avg `-0.5361` n `27`; metal avg `-1.0269` n `20`; unknown avg `234.567` n `1038`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1866`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.185`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1841`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
