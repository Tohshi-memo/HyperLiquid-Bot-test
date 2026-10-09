# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T15:22:32.265447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0146` n `13`; crypto_alt avg `-0.1272` n `235`; crypto_major avg `-0.0211` n `8`; equity avg `0.1023` n `150`; fx avg `0.001` n `6`; index avg `0.0247` n `26`; metal avg `0.0378` n `20`; unknown avg `-0.1324` n `1078`
- 1h: commodity avg `0.079` n `13`; crypto_alt avg `-0.2537` n `235`; crypto_major avg `-0.3173` n `8`; equity avg `0.1495` n `150`; fx avg `0.005` n `6`; index avg `0.0175` n `26`; metal avg `0.0146` n `20`; unknown avg `0.0415` n `1076`
- 4h: commodity avg `0.516` n `13`; crypto_alt avg `-0.2482` n `235`; crypto_major avg `-0.157` n `8`; equity avg `-0.458` n `150`; fx avg `0.002` n `6`; index avg `-0.0567` n `26`; metal avg `0.0292` n `20`; unknown avg `0.9488` n `1022`
- 24h: commodity avg `0.0409` n `13`; crypto_alt avg `0.9521` n `235`; crypto_major avg `0.487` n `8`; equity avg `-0.1258` n `150`; fx avg `0.0004` n `6`; index avg `0.0353` n `26`; metal avg `0.705` n `20`; unknown avg `30.4723` n `955`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
