# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T16:07:30.427759+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `13`; crypto_alt avg `0.0078` n `235`; crypto_major avg `-0.1012` n `8`; equity avg `-0.0134` n `150`; fx avg `0.0` n `6`; index avg `-0.0013` n `26`; metal avg `0.0064` n `20`; unknown avg `3.8697` n `1109`
- 1h: commodity avg `0.0013` n `13`; crypto_alt avg `0.0343` n `235`; crypto_major avg `-0.1968` n `8`; equity avg `-0.0059` n `150`; fx avg `-0.0011` n `6`; index avg `0.0001` n `26`; metal avg `-0.0135` n `20`; unknown avg `3.3738` n `1101`
- 4h: commodity avg `0.1133` n `13`; crypto_alt avg `0.8808` n `235`; crypto_major avg `0.5127` n `8`; equity avg `0.118` n `150`; fx avg `-0.0056` n `6`; index avg `0.0147` n `26`; metal avg `-0.0106` n `20`; unknown avg `0.9918` n `1101`
- 24h: commodity avg `-0.4428` n `13`; crypto_alt avg `2.2314` n `235`; crypto_major avg `0.7559` n `8`; equity avg `0.3998` n `150`; fx avg `0.0057` n `6`; index avg `0.0561` n `26`; metal avg `-0.0263` n `20`; unknown avg `1.4968` n `984`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
