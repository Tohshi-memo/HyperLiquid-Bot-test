# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T11:52:32.900964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `13`; crypto_alt avg `0.0765` n `235`; crypto_major avg `-0.0543` n `8`; equity avg `-0.0094` n `143`; fx avg `0.0067` n `6`; index avg `0.0006` n `26`; metal avg `0.0004` n `20`; unknown avg `0.0005` n `1079`
- 1h: commodity avg `0.0269` n `13`; crypto_alt avg `-0.0493` n `235`; crypto_major avg `-0.1268` n `8`; equity avg `-0.0035` n `143`; fx avg `0.0069` n `6`; index avg `0.0016` n `26`; metal avg `0.0015` n `20`; unknown avg `-0.0836` n `1077`
- 4h: commodity avg `0.0304` n `13`; crypto_alt avg `-0.3823` n `235`; crypto_major avg `0.2004` n `8`; equity avg `0.035` n `143`; fx avg `0.0297` n `6`; index avg `0.0134` n `26`; metal avg `-0.0061` n `20`; unknown avg `-0.1036` n `1061`
- 24h: commodity avg `0.1682` n `13`; crypto_alt avg `1.4683` n `235`; crypto_major avg `1.1953` n `8`; equity avg `0.2463` n `143`; fx avg `0.0054` n `6`; index avg `0.0405` n `26`; metal avg `-0.0064` n `20`; unknown avg `0.0206` n `900`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2075`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1801`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
