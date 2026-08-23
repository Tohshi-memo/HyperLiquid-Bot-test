# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T08:07:25.664298+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.0175` n `230`; crypto_major avg `-0.0407` n `8`; equity avg `0.0154` n `121`; fx avg `-0.052` n `6`; index avg `0.0017` n `25`; metal avg `-0.012` n `20`; unknown avg `0.0895` n `794`
- 1h: commodity avg `0.0134` n `12`; crypto_alt avg `0.5202` n `230`; crypto_major avg `0.1815` n `8`; equity avg `0.0906` n `121`; fx avg `-0.044` n `6`; index avg `0.0068` n `25`; metal avg `-0.0019` n `20`; unknown avg `0.208` n `794`
- 4h: commodity avg `0.0091` n `12`; crypto_alt avg `0.8067` n `230`; crypto_major avg `-0.4308` n `8`; equity avg `-0.0729` n `121`; fx avg `-0.0311` n `6`; index avg `-0.028` n `25`; metal avg `-0.0057` n `20`; unknown avg `0.4801` n `778`
- 24h: commodity avg `0.0029` n `12`; crypto_alt avg `-3.9058` n `230`; crypto_major avg `-2.2689` n `8`; equity avg `0.0334` n `121`; fx avg `0.0714` n `6`; index avg `-0.0025` n `25`; metal avg `0.0486` n `20`; unknown avg `2.3236` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
