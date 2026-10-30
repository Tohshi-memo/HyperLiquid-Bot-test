# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T11:22:29.405358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0297` n `13`; crypto_alt avg `-0.1512` n `238`; crypto_major avg `-0.1213` n `8`; equity avg `-0.0078` n `156`; fx avg `-0.0035` n `6`; index avg `-0.0137` n `27`; metal avg `-0.0804` n `20`; unknown avg `0.0817` n `1261`
- 1h: commodity avg `-0.0188` n `13`; crypto_alt avg `0.4331` n `238`; crypto_major avg `0.4632` n `8`; equity avg `-0.3016` n `156`; fx avg `-0.0406` n `6`; index avg `-0.028` n `27`; metal avg `-0.0568` n `20`; unknown avg `0.8778` n `1255`
- 4h: commodity avg `0.2285` n `13`; crypto_alt avg `0.4741` n `238`; crypto_major avg `-0.6289` n `8`; equity avg `-1.0478` n `156`; fx avg `0.0136` n `6`; index avg `-0.1143` n `27`; metal avg `-0.1246` n `20`; unknown avg `4.3804` n `1190`
- 24h: commodity avg `0.2905` n `13`; crypto_alt avg `-3.6708` n `238`; crypto_major avg `-1.8805` n `8`; equity avg `-4.1419` n `156`; fx avg `0.051` n `6`; index avg `-0.4781` n `27`; metal avg `-0.7635` n `20`; unknown avg `24.3836` n `1034`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
