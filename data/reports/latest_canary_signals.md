# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T22:37:29.742860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0192` n `13`; crypto_alt avg `0.3067` n `238`; crypto_major avg `0.1793` n `8`; equity avg `0.0219` n `156`; fx avg `0.0099` n `6`; index avg `-0.0036` n `27`; metal avg `0.0047` n `20`; unknown avg `-0.0962` n `1261`
- 1h: commodity avg `-0.0195` n `13`; crypto_alt avg `0.3259` n `238`; crypto_major avg `-0.0119` n `8`; equity avg `0.0584` n `156`; fx avg `0.0002` n `6`; index avg `0.0016` n `27`; metal avg `0.0327` n `20`; unknown avg `198.9913` n `1255`
- 4h: commodity avg `-0.2712` n `13`; crypto_alt avg `1.7115` n `238`; crypto_major avg `0.6155` n `8`; equity avg `1.5499` n `156`; fx avg `-0.023` n `6`; index avg `0.1633` n `27`; metal avg `0.1188` n `20`; unknown avg `0.9384` n `1149`
- 24h: commodity avg `0.049` n `13`; crypto_alt avg `0.8425` n `238`; crypto_major avg `-1.4528` n `8`; equity avg `-2.9076` n `156`; fx avg `-0.1386` n `6`; index avg `-0.2601` n `27`; metal avg `-0.9636` n `20`; unknown avg `0.8739` n `1016`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
