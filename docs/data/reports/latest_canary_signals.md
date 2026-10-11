# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T10:22:29.726186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `13`; crypto_alt avg `-0.093` n `235`; crypto_major avg `-0.0062` n `8`; equity avg `0.0046` n `150`; fx avg `-0.0002` n `6`; index avg `0.0012` n `26`; metal avg `0.0014` n `20`; unknown avg `-0.0287` n `1117`
- 1h: commodity avg `0.0078` n `13`; crypto_alt avg `-0.1057` n `235`; crypto_major avg `0.0004` n `8`; equity avg `0.0073` n `150`; fx avg `0.0099` n `6`; index avg `0.0023` n `26`; metal avg `-0.0021` n `20`; unknown avg `0.4544` n `1115`
- 4h: commodity avg `0.0373` n `13`; crypto_alt avg `0.1833` n `235`; crypto_major avg `0.0233` n `8`; equity avg `0.0716` n `150`; fx avg `0.0107` n `6`; index avg `0.0096` n `26`; metal avg `0.0111` n `20`; unknown avg `0.1724` n `1099`
- 24h: commodity avg `0.4369` n `13`; crypto_alt avg `1.2799` n `235`; crypto_major avg `-0.0011` n `8`; equity avg `0.1196` n `150`; fx avg `0.0105` n `6`; index avg `-0.0055` n `26`; metal avg `0.0055` n `20`; unknown avg `0.6476` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
