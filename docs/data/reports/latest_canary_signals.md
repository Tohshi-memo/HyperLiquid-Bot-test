# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T08:37:35.765872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `13`; crypto_alt avg `-0.2215` n `235`; crypto_major avg `-0.1692` n `8`; equity avg `-0.0502` n `150`; fx avg `-0.014` n `6`; index avg `-0.003` n `26`; metal avg `-0.0207` n `20`; unknown avg `2.1675` n `1077`
- 1h: commodity avg `0.0484` n `13`; crypto_alt avg `-0.5424` n `235`; crypto_major avg `-0.5586` n `8`; equity avg `-0.0583` n `150`; fx avg `-0.0011` n `6`; index avg `0.0105` n `26`; metal avg `0.0143` n `20`; unknown avg `1.3231` n `1059`
- 4h: commodity avg `0.4529` n `13`; crypto_alt avg `0.2602` n `235`; crypto_major avg `0.0059` n `8`; equity avg `-0.7387` n `150`; fx avg `0.0035` n `6`; index avg `-0.1335` n `26`; metal avg `-0.1702` n `20`; unknown avg `0.562` n `1031`
- 24h: commodity avg `0.8575` n `13`; crypto_alt avg `-1.0448` n `235`; crypto_major avg `-2.4765` n `8`; equity avg `-1.7864` n `150`; fx avg `-0.0255` n `6`; index avg `-0.3053` n `26`; metal avg `-0.2254` n `20`; unknown avg `416.7401` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
