# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T11:52:30.289480+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `13`; crypto_alt avg `-0.0193` n `239`; crypto_major avg `0.0295` n `8`; equity avg `-0.0679` n `166`; fx avg `-0.008` n `6`; index avg `-0.0111` n `27`; metal avg `-0.0063` n `20`; unknown avg `0.3846` n `1256`
- 1h: commodity avg `0.0315` n `13`; crypto_alt avg `0.296` n `239`; crypto_major avg `0.5681` n `8`; equity avg `0.1553` n `166`; fx avg `0.0156` n `6`; index avg `0.0072` n `27`; metal avg `-0.0029` n `20`; unknown avg `2.3212` n `1228`
- 4h: commodity avg `0.0014` n `13`; crypto_alt avg `0.6373` n `239`; crypto_major avg `0.9714` n `8`; equity avg `0.09` n `166`; fx avg `0.0453` n `6`; index avg `0.0029` n `27`; metal avg `0.0586` n `20`; unknown avg `2.0722` n `1212`
- 24h: commodity avg `0.5116` n `13`; crypto_alt avg `-4.5594` n `239`; crypto_major avg `-5.086` n `8`; equity avg `-4.1246` n `166`; fx avg `-0.0762` n `6`; index avg `-0.4754` n `27`; metal avg `-0.4231` n `20`; unknown avg `-0.0874` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
