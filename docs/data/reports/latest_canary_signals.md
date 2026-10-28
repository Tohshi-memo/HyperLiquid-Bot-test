# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T23:22:26.734367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `13`; crypto_alt avg `-0.0124` n `238`; crypto_major avg `0.027` n `8`; equity avg `-0.0063` n `155`; fx avg `0.0056` n `6`; index avg `-0.0042` n `27`; metal avg `0.0045` n `20`; unknown avg `164.249` n `1238`
- 1h: commodity avg `-0.0165` n `13`; crypto_alt avg `-0.1185` n `238`; crypto_major avg `0.0205` n `8`; equity avg `0.0211` n `155`; fx avg `-0.0025` n `6`; index avg `0.0253` n `27`; metal avg `0.0118` n `20`; unknown avg `2.7062` n `1168`
- 4h: commodity avg `-0.2317` n `13`; crypto_alt avg `0.1584` n `238`; crypto_major avg `0.1752` n `8`; equity avg `-0.6809` n `155`; fx avg `-0.0107` n `6`; index avg `-0.0789` n `27`; metal avg `0.04` n `20`; unknown avg `1.1669` n `1064`
- 24h: commodity avg `0.1586` n `13`; crypto_alt avg `0.6473` n `238`; crypto_major avg `0.5601` n `8`; equity avg `1.0341` n `154`; fx avg `0.2446` n `6`; index avg `0.1662` n `27`; metal avg `-0.1422` n `20`; unknown avg `25.6462` n `1010`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
