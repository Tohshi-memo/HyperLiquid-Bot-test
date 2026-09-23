# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T13:37:33.739090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `0.1034` n `234`; crypto_major avg `0.2944` n `8`; equity avg `-0.4015` n `140`; fx avg `-0.0118` n `6`; index avg `-0.0304` n `26`; metal avg `-0.029` n `20`; unknown avg `396.1506` n `944`
- 1h: commodity avg `-0.115` n `12`; crypto_alt avg `-0.4198` n `234`; crypto_major avg `0.0393` n `8`; equity avg `-0.2242` n `140`; fx avg `-0.0315` n `6`; index avg `-0.0255` n `26`; metal avg `-0.0482` n `20`; unknown avg `11.4934` n `942`
- 4h: commodity avg `0.0516` n `12`; crypto_alt avg `-1.0695` n `234`; crypto_major avg `-0.514` n `8`; equity avg `-0.687` n `140`; fx avg `0.0001` n `6`; index avg `-0.0964` n `26`; metal avg `-0.2311` n `20`; unknown avg `11.084` n `935`
- 24h: commodity avg `0.5633` n `12`; crypto_alt avg `2.111` n `234`; crypto_major avg `-0.1399` n `8`; equity avg `-0.2353` n `140`; fx avg `-0.0375` n `6`; index avg `-0.0838` n `26`; metal avg `-0.4906` n `20`; unknown avg `6.5955` n `840`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
