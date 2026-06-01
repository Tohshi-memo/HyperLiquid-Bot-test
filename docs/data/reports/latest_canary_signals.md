# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T03:22:24.053707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0306` n `12`; crypto_alt avg `-0.0845` n `228`; crypto_major avg `-0.0494` n `8`; equity avg `-0.0387` n `69`; fx avg `0.0056` n `6`; index avg `-0.0057` n `23`; metal avg `-0.069` n `18`; unknown avg `0.0002` n `422`
- 1h: commodity avg `-0.0507` n `12`; crypto_alt avg `0.8963` n `228`; crypto_major avg `0.5442` n `8`; equity avg `0.1351` n `69`; fx avg `0.0098` n `6`; index avg `0.5453` n `23`; metal avg `-0.2676` n `18`; unknown avg `0.3563` n `422`
- 4h: commodity avg `0.1836` n `12`; crypto_alt avg `1.0506` n `228`; crypto_major avg `0.3001` n `8`; equity avg `0.171` n `69`; fx avg `0.0973` n `6`; index avg `0.5945` n `23`; metal avg `0.0758` n `18`; unknown avg `0.4998` n `421`
- 24h: commodity avg `0.9881` n `12`; crypto_alt avg `1.3217` n `228`; crypto_major avg `-0.0114` n `8`; equity avg `0.6189` n `69`; fx avg `0.0536` n `6`; index avg `0.6326` n `23`; metal avg `0.204` n `18`; unknown avg `1.8512` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2867`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2407`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2034`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
