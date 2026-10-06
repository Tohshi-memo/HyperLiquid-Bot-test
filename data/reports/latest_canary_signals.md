# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T14:52:44.719961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.065` n `13`; crypto_alt avg `0.2836` n `235`; crypto_major avg `0.248` n `8`; equity avg `0.2944` n `150`; fx avg `-0.0029` n `6`; index avg `0.0409` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.2559` n `1072`
- 1h: commodity avg `-0.062` n `13`; crypto_alt avg `0.2233` n `235`; crypto_major avg `0.0736` n `8`; equity avg `0.0592` n `150`; fx avg `0.0075` n `6`; index avg `0.0028` n `26`; metal avg `-0.0366` n `20`; unknown avg `4.8669` n `1024`
- 4h: commodity avg `0.1513` n `13`; crypto_alt avg `0.2094` n `235`; crypto_major avg `0.2507` n `8`; equity avg `0.4148` n `150`; fx avg `0.0304` n `6`; index avg `0.0433` n `26`; metal avg `-0.1186` n `20`; unknown avg `5.0288` n `1018`
- 24h: commodity avg `-0.5825` n `13`; crypto_alt avg `0.9033` n `235`; crypto_major avg `0.7245` n `8`; equity avg `0.9837` n `149`; fx avg `0.1108` n `6`; index avg `0.165` n `26`; metal avg `-0.1653` n `20`; unknown avg `393.3507` n `884`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
