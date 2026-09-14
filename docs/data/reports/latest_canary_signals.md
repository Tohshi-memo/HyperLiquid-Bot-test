# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T13:22:43.932446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0668` n `12`; crypto_alt avg `0.4331` n `233`; crypto_major avg `0.4235` n `8`; equity avg `0.2204` n `136`; fx avg `0.0144` n `6`; index avg `0.0694` n `27`; metal avg `0.0668` n `20`; unknown avg `1.9437` n `894`
- 1h: commodity avg `0.0204` n `12`; crypto_alt avg `-0.6315` n `233`; crypto_major avg `-0.4459` n `8`; equity avg `-0.1491` n `136`; fx avg `0.0374` n `6`; index avg `-0.0254` n `27`; metal avg `-0.0285` n `20`; unknown avg `51.8762` n `886`
- 4h: commodity avg `-0.082` n `12`; crypto_alt avg `-0.2701` n `233`; crypto_major avg `0.0103` n `8`; equity avg `-0.1306` n `136`; fx avg `0.0646` n `6`; index avg `0.0174` n `27`; metal avg `0.0937` n `20`; unknown avg `2.6601` n `886`
- 24h: commodity avg `0.5451` n `12`; crypto_alt avg `-0.2895` n `233`; crypto_major avg `1.6409` n `8`; equity avg `-1.0767` n `136`; fx avg `0.0881` n `6`; index avg `-0.2291` n `27`; metal avg `-0.4479` n `20`; unknown avg `1.2469` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
