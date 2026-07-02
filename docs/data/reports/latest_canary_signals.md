# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T05:07:32.640170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `-0.0124` n `228`; crypto_major avg `-0.1257` n `8`; equity avg `0.1682` n `88`; fx avg `0.002` n `6`; index avg `0.0648` n `25`; metal avg `-0.0376` n `20`; unknown avg `0.2771` n `763`
- 1h: commodity avg `0.0246` n `12`; crypto_alt avg `-0.0424` n `228`; crypto_major avg `-0.1087` n `8`; equity avg `-0.0458` n `88`; fx avg `0.026` n `6`; index avg `0.0241` n `25`; metal avg `-0.1577` n `20`; unknown avg `-0.0326` n `763`
- 4h: commodity avg `-0.0029` n `12`; crypto_alt avg `1.2303` n `228`; crypto_major avg `1.3978` n `8`; equity avg `-0.0695` n `88`; fx avg `-0.0187` n `6`; index avg `0.0668` n `25`; metal avg `0.1073` n `20`; unknown avg `0.237` n `759`
- 24h: commodity avg `-0.6348` n `12`; crypto_alt avg `1.3545` n `228`; crypto_major avg `0.862` n `8`; equity avg `-1.5439` n `88`; fx avg `0.002` n `6`; index avg `-0.3809` n `25`; metal avg `1.089` n `20`; unknown avg `24.9344` n `735`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
