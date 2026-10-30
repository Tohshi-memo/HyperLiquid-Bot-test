# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T12:52:26.829652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0362` n `13`; crypto_alt avg `-0.0698` n `238`; crypto_major avg `-0.1269` n `8`; equity avg `-0.0696` n `156`; fx avg `-0.0242` n `6`; index avg `-0.0012` n `27`; metal avg `-0.0593` n `20`; unknown avg `90.4825` n `1261`
- 1h: commodity avg `-0.0834` n `13`; crypto_alt avg `0.0245` n `238`; crypto_major avg `-0.0645` n `8`; equity avg `-0.1911` n `156`; fx avg `-0.0305` n `6`; index avg `-0.0047` n `27`; metal avg `-0.0569` n `20`; unknown avg `19.7916` n `1249`
- 4h: commodity avg `-0.0351` n `13`; crypto_alt avg `0.6637` n `238`; crypto_major avg `-0.1645` n `8`; equity avg `-1.131` n `156`; fx avg `-0.0522` n `6`; index avg `-0.1136` n `27`; metal avg `-0.3056` n `20`; unknown avg `6.637` n `1249`
- 24h: commodity avg `0.4387` n `13`; crypto_alt avg `-4.1024` n `238`; crypto_major avg `-2.7244` n `8`; equity avg `-4.2701` n `156`; fx avg `0.0182` n `6`; index avg `-0.427` n `27`; metal avg `-0.7855` n `20`; unknown avg `22.7305` n `1032`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
