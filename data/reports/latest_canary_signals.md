# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T20:37:27.414754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `13`; crypto_alt avg `-0.1982` n `235`; crypto_major avg `-0.1091` n `8`; equity avg `-0.0163` n `150`; fx avg `-0.006` n `6`; index avg `-0.0041` n `26`; metal avg `-0.006` n `20`; unknown avg `-0.1126` n `1116`
- 1h: commodity avg `0.0309` n `13`; crypto_alt avg `0.2382` n `235`; crypto_major avg `-0.0413` n `8`; equity avg `0.0936` n `150`; fx avg `0.0036` n `6`; index avg `0.0037` n `26`; metal avg `0.0048` n `20`; unknown avg `0.2878` n `1040`
- 4h: commodity avg `-0.2626` n `13`; crypto_alt avg `-0.2663` n `235`; crypto_major avg `-0.4041` n `8`; equity avg `0.1225` n `150`; fx avg `0.02` n `6`; index avg `0.0163` n `26`; metal avg `0.0562` n `20`; unknown avg `1.1203` n `1032`
- 24h: commodity avg `-0.0674` n `13`; crypto_alt avg `1.2005` n `235`; crypto_major avg `0.1631` n `8`; equity avg `0.8606` n `150`; fx avg `0.0079` n `6`; index avg `0.1362` n `26`; metal avg `0.6228` n `20`; unknown avg `13.2933` n `909`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
