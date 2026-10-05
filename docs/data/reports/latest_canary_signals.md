# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T11:52:32.804547+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `13`; crypto_alt avg `0.0708` n `235`; crypto_major avg `-0.0445` n `8`; equity avg `-0.0952` n `144`; fx avg `0.0116` n `6`; index avg `-0.0084` n `26`; metal avg `-0.0712` n `20`; unknown avg `2.055` n `1079`
- 1h: commodity avg `-0.0892` n `13`; crypto_alt avg `0.0985` n `235`; crypto_major avg `0.007` n `8`; equity avg `-0.0193` n `144`; fx avg `0.0326` n `6`; index avg `0.0415` n `26`; metal avg `0.0213` n `20`; unknown avg `0.7506` n `1077`
- 4h: commodity avg `0.1235` n `13`; crypto_alt avg `-0.2895` n `235`; crypto_major avg `-0.2385` n `8`; equity avg `-0.2616` n `144`; fx avg `0.0577` n `6`; index avg `-0.0155` n `26`; metal avg `-0.0348` n `20`; unknown avg `48.0743` n `997`
- 24h: commodity avg `-0.1994` n `13`; crypto_alt avg `1.1963` n `235`; crypto_major avg `1.0956` n `8`; equity avg `0.0631` n `144`; fx avg `-0.037` n `6`; index avg `-0.0434` n `26`; metal avg `0.2485` n `20`; unknown avg `0.8322` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2139`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1968`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
