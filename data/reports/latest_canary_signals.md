# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T08:51:17.290654+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0315` n `13`; crypto_alt avg `0.1412` n `238`; crypto_major avg `0.1719` n `8`; equity avg `0.009` n `156`; fx avg `0.0007` n `6`; index avg `-0.0019` n `27`; metal avg `0.0126` n `20`; unknown avg `0.1145` n `1262`
- 1h: commodity avg `0.0348` n `13`; crypto_alt avg `0.086` n `238`; crypto_major avg `-0.1852` n `8`; equity avg `-0.0135` n `156`; fx avg `0.0048` n `6`; index avg `-0.0012` n `27`; metal avg `0.0053` n `20`; unknown avg `202.2078` n `1238`
- 4h: commodity avg `0.021` n `13`; crypto_alt avg `-0.3011` n `238`; crypto_major avg `-0.2593` n `8`; equity avg `-0.0246` n `156`; fx avg `0.0199` n `6`; index avg `0.006` n `27`; metal avg `-0.0027` n `20`; unknown avg `0.8672` n `1210`
- 24h: commodity avg `-0.1872` n `13`; crypto_alt avg `0.833` n `238`; crypto_major avg `-1.0763` n `8`; equity avg `-2.1203` n `156`; fx avg `-0.0633` n `6`; index avg `-0.21` n `27`; metal avg `-0.5051` n `20`; unknown avg `5.0628` n `1043`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
