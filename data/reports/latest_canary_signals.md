# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T01:52:29.793449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `12`; crypto_alt avg `-0.1776` n `234`; crypto_major avg `-0.171` n `8`; equity avg `-0.2148` n `137`; fx avg `0.0491` n `6`; index avg `-0.037` n `27`; metal avg `-0.0908` n `20`; unknown avg `1.1594` n `919`
- 1h: commodity avg `0.2417` n `12`; crypto_alt avg `0.4226` n `234`; crypto_major avg `0.4624` n `8`; equity avg `0.016` n `137`; fx avg `0.0592` n `6`; index avg `0.0065` n `27`; metal avg `0.2202` n `20`; unknown avg `0.263` n `917`
- 4h: commodity avg `0.0376` n `12`; crypto_alt avg `1.539` n `234`; crypto_major avg `0.9035` n `8`; equity avg `0.58` n `137`; fx avg `0.0414` n `6`; index avg `0.1367` n `27`; metal avg `0.3144` n `20`; unknown avg `1.2585` n `813`
- 24h: commodity avg `-0.54` n `12`; crypto_alt avg `2.749` n `234`; crypto_major avg `1.9782` n `8`; equity avg `1.7441` n `137`; fx avg `-0.007` n `6`; index avg `0.1832` n `27`; metal avg `0.0634` n `20`; unknown avg `1.7585` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
