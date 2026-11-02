# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T15:07:29.367706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0424` n `13`; crypto_alt avg `-0.0266` n `239`; crypto_major avg `-0.0058` n `8`; equity avg `0.4947` n `156`; fx avg `0.0151` n `6`; index avg `0.0327` n `27`; metal avg `-0.0259` n `20`; unknown avg `0.1415` n `1259`
- 1h: commodity avg `-0.1222` n `13`; crypto_alt avg `-0.2237` n `239`; crypto_major avg `-0.0928` n `8`; equity avg `-0.9093` n `156`; fx avg `0.0134` n `6`; index avg `-0.0243` n `27`; metal avg `0.0921` n `20`; unknown avg `0.1476` n `1259`
- 4h: commodity avg `-0.454` n `13`; crypto_alt avg `0.0696` n `238`; crypto_major avg `0.1107` n `8`; equity avg `-1.2647` n `156`; fx avg `0.0219` n `6`; index avg `-0.0113` n `27`; metal avg `0.2659` n `20`; unknown avg `284.5484` n `1252`
- 24h: commodity avg `-1.0153` n `13`; crypto_alt avg `-2.1979` n `238`; crypto_major avg `-0.6177` n `8`; equity avg `-0.3995` n `156`; fx avg `0.2708` n `6`; index avg `0.2393` n `27`; metal avg `0.3314` n `20`; unknown avg `7.7161` n `1077`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
