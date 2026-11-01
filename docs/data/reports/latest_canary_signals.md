# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T01:22:34.352457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.012` n `13`; crypto_alt avg `-0.025` n `238`; crypto_major avg `0.0027` n `8`; equity avg `0.0039` n `156`; fx avg `-0.0078` n `6`; index avg `0.0` n `27`; metal avg `0.0023` n `20`; unknown avg `-0.13` n `1260`
- 1h: commodity avg `-0.0797` n `13`; crypto_alt avg `0.2534` n `238`; crypto_major avg `0.2799` n `8`; equity avg `0.045` n `156`; fx avg `0.0033` n `6`; index avg `-0.0292` n `27`; metal avg `0.0016` n `20`; unknown avg `1.3229` n `1242`
- 4h: commodity avg `0.0328` n `13`; crypto_alt avg `0.0864` n `238`; crypto_major avg `0.2737` n `8`; equity avg `0.0194` n `156`; fx avg `-0.0007` n `6`; index avg `-0.017` n `27`; metal avg `0.015` n `20`; unknown avg `1.4449` n `1098`
- 24h: commodity avg `0.0458` n `13`; crypto_alt avg `-0.6014` n `238`; crypto_major avg `-0.2855` n `8`; equity avg `-0.028` n `156`; fx avg `-0.0029` n `6`; index avg `-0.0869` n `27`; metal avg `0.0429` n `20`; unknown avg `1.8864` n `1006`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
