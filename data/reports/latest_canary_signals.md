# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T09:07:26.071882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0556` n `13`; crypto_alt avg `0.1229` n `238`; crypto_major avg `0.0113` n `8`; equity avg `0.1384` n `156`; fx avg `0.0194` n `6`; index avg `0.033` n `27`; metal avg `0.0082` n `20`; unknown avg `14.926` n `1255`
- 1h: commodity avg `-0.0706` n `13`; crypto_alt avg `0.1883` n `238`; crypto_major avg `0.0599` n `8`; equity avg `0.2708` n `156`; fx avg `0.0086` n `6`; index avg `0.0154` n `27`; metal avg `0.1141` n `20`; unknown avg `46.9682` n `1242`
- 4h: commodity avg `0.1589` n `13`; crypto_alt avg `0.0216` n `238`; crypto_major avg `-0.9061` n `8`; equity avg `-0.7174` n `156`; fx avg `0.0163` n `6`; index avg `0.007` n `27`; metal avg `-0.1768` n `20`; unknown avg `3.8594` n `1172`
- 24h: commodity avg `0.1822` n `13`; crypto_alt avg `-3.5485` n `238`; crypto_major avg `-0.9283` n `8`; equity avg `-3.2282` n `155`; fx avg `0.1412` n `6`; index avg `-0.3588` n `27`; metal avg `-0.6449` n `20`; unknown avg `31.7678` n `938`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
