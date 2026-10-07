# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T22:52:30.107406+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0245` n `13`; crypto_alt avg `0.0671` n `235`; crypto_major avg `-0.0213` n `8`; equity avg `-0.0263` n `150`; fx avg `0.0019` n `6`; index avg `0.0012` n `26`; metal avg `0.0094` n `20`; unknown avg `0.8587` n `1077`
- 1h: commodity avg `0.0893` n `13`; crypto_alt avg `0.7028` n `235`; crypto_major avg `0.3045` n `8`; equity avg `0.0374` n `150`; fx avg `-0.0023` n `6`; index avg `0.0266` n `26`; metal avg `-0.0304` n `20`; unknown avg `0.6025` n `1075`
- 4h: commodity avg `0.2548` n `13`; crypto_alt avg `0.5463` n `235`; crypto_major avg `-0.1888` n `8`; equity avg `0.0164` n `150`; fx avg `0.0315` n `6`; index avg `0.0132` n `26`; metal avg `-0.0537` n `20`; unknown avg `0.3115` n `999`
- 24h: commodity avg `0.4856` n `13`; crypto_alt avg `-3.6791` n `235`; crypto_major avg `-3.4194` n `8`; equity avg `-1.3526` n `150`; fx avg `-0.1425` n `6`; index avg `-0.1997` n `26`; metal avg `-0.6821` n `20`; unknown avg `248.1639` n `980`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
