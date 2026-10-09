# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T19:37:29.581316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0084` n `13`; crypto_alt avg `-0.3733` n `235`; crypto_major avg `-0.2246` n `8`; equity avg `-0.1751` n `150`; fx avg `-0.0065` n `6`; index avg `-0.0244` n `26`; metal avg `-0.0002` n `20`; unknown avg `9.4249` n `1092`
- 1h: commodity avg `-0.204` n `13`; crypto_alt avg `-0.6329` n `235`; crypto_major avg `-0.3416` n `8`; equity avg `-0.1199` n `150`; fx avg `-0.0087` n `6`; index avg `-0.0097` n `26`; metal avg `-0.0149` n `20`; unknown avg `10.2645` n `1090`
- 4h: commodity avg `-0.4206` n `13`; crypto_alt avg `-0.2929` n `235`; crypto_major avg `-0.4406` n `8`; equity avg `0.1057` n `150`; fx avg `-0.0057` n `6`; index avg `0.0383` n `26`; metal avg `0.0074` n `20`; unknown avg `10.1759` n `1050`
- 24h: commodity avg `-0.1784` n `13`; crypto_alt avg `1.5673` n `235`; crypto_major avg `0.5157` n `8`; equity avg `1.1507` n `150`; fx avg `0.0192` n `6`; index avg `0.1883` n `26`; metal avg `0.6295` n `20`; unknown avg `5.4803` n `915`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
