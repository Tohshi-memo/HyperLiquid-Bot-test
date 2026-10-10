# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T08:37:28.259910+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `13`; crypto_alt avg `0.0815` n `235`; crypto_major avg `0.0283` n `8`; equity avg `0.0128` n `150`; fx avg `-0.0288` n `6`; index avg `-0.0066` n `26`; metal avg `-0.0059` n `20`; unknown avg `0.9568` n `1117`
- 1h: commodity avg `-0.0245` n `13`; crypto_alt avg `-0.1521` n `235`; crypto_major avg `0.0661` n `8`; equity avg `-0.013` n `150`; fx avg `0.0072` n `6`; index avg `-0.0068` n `26`; metal avg `-0.0014` n `20`; unknown avg `0.3932` n `1099`
- 4h: commodity avg `0.0106` n `13`; crypto_alt avg `-0.1521` n `235`; crypto_major avg `0.1999` n `8`; equity avg `-0.0842` n `150`; fx avg `0.0065` n `6`; index avg `-0.0381` n `26`; metal avg `-0.0092` n `20`; unknown avg `0.7109` n `1082`
- 24h: commodity avg `0.1192` n `13`; crypto_alt avg `1.2704` n `235`; crypto_major avg `0.1267` n `8`; equity avg `-0.3224` n `150`; fx avg `-0.048` n `6`; index avg `-0.0667` n `26`; metal avg `-0.0204` n `20`; unknown avg `632.6773` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
