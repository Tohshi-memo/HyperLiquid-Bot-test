# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T13:52:27.868918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0918` n `13`; crypto_alt avg `-0.5894` n `238`; crypto_major avg `-0.6658` n `8`; equity avg `-0.2151` n `156`; fx avg `-0.0485` n `6`; index avg `-0.0212` n `27`; metal avg `-0.1141` n `20`; unknown avg `-0.1043` n `1261`
- 1h: commodity avg `0.0453` n `13`; crypto_alt avg `-0.8899` n `238`; crypto_major avg `-0.9868` n `8`; equity avg `-0.0249` n `156`; fx avg `-0.0662` n `6`; index avg `0.0094` n `27`; metal avg `-0.1466` n `20`; unknown avg `1.8624` n `1251`
- 4h: commodity avg `-0.0245` n `13`; crypto_alt avg `-0.2945` n `238`; crypto_major avg `-0.9275` n `8`; equity avg `-0.7328` n `156`; fx avg `-0.1455` n `6`; index avg `-0.0606` n `27`; metal avg `-0.4226` n `20`; unknown avg `1.6263` n `1247`
- 24h: commodity avg `0.6928` n `13`; crypto_alt avg `-5.1213` n `238`; crypto_major avg `-3.9327` n `8`; equity avg `-4.3769` n `156`; fx avg `0.0006` n `6`; index avg `-0.35` n `27`; metal avg `-0.8682` n `20`; unknown avg `3487.988` n `1038`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1706`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
