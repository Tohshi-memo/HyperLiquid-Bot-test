# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T22:52:42.266736+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `13`; crypto_alt avg `0.1739` n `239`; crypto_major avg `0.1796` n `8`; equity avg `0.012` n `158`; fx avg `-0.0074` n `6`; index avg `0.0031` n `27`; metal avg `-0.0071` n `20`; unknown avg `18.9292` n `1256`
- 1h: commodity avg `-0.0099` n `13`; crypto_alt avg `-0.0462` n `239`; crypto_major avg `-0.0926` n `8`; equity avg `-0.0431` n `158`; fx avg `-0.0302` n `6`; index avg `0.004` n `27`; metal avg `0.007` n `20`; unknown avg `159.6586` n `1250`
- 4h: commodity avg `0.1896` n `13`; crypto_alt avg `0.3879` n `239`; crypto_major avg `0.2065` n `8`; equity avg `0.8843` n `158`; fx avg `-0.0176` n `6`; index avg `0.0794` n `27`; metal avg `-0.0071` n `20`; unknown avg `188.6728` n `1207`
- 24h: commodity avg `0.3631` n `13`; crypto_alt avg `1.2102` n `239`; crypto_major avg `1.3487` n `8`; equity avg `2.551` n `158`; fx avg `0.0648` n `6`; index avg `0.2807` n `27`; metal avg `-0.5047` n `20`; unknown avg `-1.2832` n `1057`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
