# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T06:52:31.313212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `0.1713` n `232`; crypto_major avg `0.0727` n `8`; equity avg `0.0238` n `132`; fx avg `-0.0253` n `6`; index avg `0.0232` n `26`; metal avg `0.0078` n `20`; unknown avg `0.2431` n `792`
- 1h: commodity avg `0.0439` n `12`; crypto_alt avg `-0.2645` n `232`; crypto_major avg `-0.291` n `8`; equity avg `-0.2055` n `132`; fx avg `-0.0544` n `6`; index avg `-0.0366` n `26`; metal avg `-0.0487` n `20`; unknown avg `-0.1604` n `770`
- 4h: commodity avg `0.0017` n `12`; crypto_alt avg `0.4481` n `232`; crypto_major avg `0.2997` n `8`; equity avg `-0.0558` n `132`; fx avg `-0.1339` n `6`; index avg `-0.0551` n `26`; metal avg `0.0908` n `20`; unknown avg `0.0864` n `770`
- 24h: commodity avg `0.9056` n `12`; crypto_alt avg `-0.7054` n `232`; crypto_major avg `-1.7858` n `8`; equity avg `-2.6033` n `130`; fx avg `-0.1912` n `6`; index avg `-0.4877` n `26`; metal avg `-0.9347` n `20`; unknown avg `-0.4632` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0447`, n `668`, weak_sample_signal
