# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T02:37:34.344019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0224` n `12`; crypto_alt avg `-0.1056` n `228`; crypto_major avg `0.014` n `8`; equity avg `0.0057` n `74`; fx avg `-0.0264` n `6`; index avg `-0.0477` n `23`; metal avg `0.0063` n `18`; unknown avg `2.2203` n `645`
- 1h: commodity avg `-0.0133` n `12`; crypto_alt avg `0.1288` n `228`; crypto_major avg `0.1232` n `8`; equity avg `0.0254` n `74`; fx avg `0.0109` n `6`; index avg `-0.0632` n `23`; metal avg `-0.007` n `18`; unknown avg `85.2262` n `645`
- 4h: commodity avg `-0.3671` n `12`; crypto_alt avg `-0.2379` n `228`; crypto_major avg `0.2203` n `8`; equity avg `0.0749` n `74`; fx avg `0.0019` n `6`; index avg `-0.0747` n `23`; metal avg `0.004` n `18`; unknown avg `56.8369` n `645`
- 24h: commodity avg `-0.7592` n `12`; crypto_alt avg `1.4903` n `228`; crypto_major avg `1.429` n `8`; equity avg `0.3027` n `74`; fx avg `0.0107` n `6`; index avg `0.1596` n `23`; metal avg `0.2517` n `18`; unknown avg `5.0231` n `611`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
