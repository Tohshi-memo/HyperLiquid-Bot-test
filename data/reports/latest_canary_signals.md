# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T13:07:28.965870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1064` n `13`; crypto_alt avg `-0.1999` n `238`; crypto_major avg `-0.2099` n `8`; equity avg `-0.0265` n `156`; fx avg `0.002` n `6`; index avg `-0.0005` n `27`; metal avg `-0.1016` n `20`; unknown avg `0.285` n `1255`
- 1h: commodity avg `-0.1932` n `13`; crypto_alt avg `-0.1556` n `238`; crypto_major avg `-0.1978` n `8`; equity avg `-0.3225` n `156`; fx avg `-0.0356` n `6`; index avg `-0.0161` n `27`; metal avg `-0.198` n `20`; unknown avg `33.6928` n `1255`
- 4h: commodity avg `-0.0856` n `13`; crypto_alt avg `0.3398` n `238`; crypto_major avg `-0.3852` n `8`; equity avg `-1.2933` n `156`; fx avg `-0.0696` n `6`; index avg `-0.1467` n `27`; metal avg `-0.4143` n `20`; unknown avg `1.1598` n `1251`
- 24h: commodity avg `0.4887` n `13`; crypto_alt avg `-4.4857` n `238`; crypto_major avg `-3.1631` n `8`; equity avg `-4.4603` n `156`; fx avg `0.0469` n `6`; index avg `-0.466` n `27`; metal avg `-0.9235` n `20`; unknown avg `23.1317` n `1032`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
