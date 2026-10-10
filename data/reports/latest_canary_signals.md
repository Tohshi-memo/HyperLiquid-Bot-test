# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T14:22:27.467474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `13`; crypto_alt avg `0.1873` n `235`; crypto_major avg `0.2527` n `8`; equity avg `0.0153` n `150`; fx avg `0.0` n `6`; index avg `0.0074` n `26`; metal avg `0.0027` n `20`; unknown avg `0.2534` n `1117`
- 1h: commodity avg `-0.0039` n `13`; crypto_alt avg `0.2767` n `235`; crypto_major avg `0.2312` n `8`; equity avg `0.0049` n `150`; fx avg `-0.0088` n `6`; index avg `0.0077` n `26`; metal avg `0.0073` n `20`; unknown avg `0.6612` n `1115`
- 4h: commodity avg `0.0837` n `13`; crypto_alt avg `0.5422` n `235`; crypto_major avg `0.3401` n `8`; equity avg `0.0557` n `150`; fx avg `-0.0025` n `6`; index avg `-0.0067` n `26`; metal avg `0.0057` n `20`; unknown avg `1.0559` n `1109`
- 24h: commodity avg `-0.4794` n `13`; crypto_alt avg `2.3316` n `235`; crypto_major avg `0.4779` n `8`; equity avg `0.4333` n `150`; fx avg `0.0062` n `6`; index avg `0.0602` n `26`; metal avg `0.0199` n `20`; unknown avg `1.0724` n `936`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
