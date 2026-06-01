# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T17:07:25.333741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2609` n `12`; crypto_alt avg `0.454` n `228`; crypto_major avg `0.4817` n `8`; equity avg `0.1935` n `69`; fx avg `0.0101` n `6`; index avg `0.0137` n `23`; metal avg `-0.0284` n `18`; unknown avg `0.3128` n `422`
- 1h: commodity avg `-0.3064` n `12`; crypto_alt avg `1.6444` n `228`; crypto_major avg `1.2288` n `8`; equity avg `0.4023` n `69`; fx avg `0.0484` n `6`; index avg `0.1468` n `23`; metal avg `0.0117` n `18`; unknown avg `1.3067` n `422`
- 4h: commodity avg `0.7742` n `12`; crypto_alt avg `1.6846` n `228`; crypto_major avg `-0.2074` n `8`; equity avg `0.9242` n `69`; fx avg `0.038` n `6`; index avg `0.065` n `23`; metal avg `-0.3413` n `18`; unknown avg `0.418` n `422`
- 24h: commodity avg `0.7651` n `12`; crypto_alt avg `2.0541` n `228`; crypto_major avg `-0.3872` n `8`; equity avg `0.4258` n `69`; fx avg `0.0232` n `6`; index avg `0.2416` n `23`; metal avg `-0.1837` n `18`; unknown avg `4.0995` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2868`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2197`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
