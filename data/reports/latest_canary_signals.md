# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T16:22:30.681098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0253` n `13`; crypto_alt avg `-0.1055` n `235`; crypto_major avg `-0.1885` n `8`; equity avg `-0.0449` n `150`; fx avg `-0.0067` n `6`; index avg `-0.0085` n `26`; metal avg `-0.0261` n `20`; unknown avg `0.0605` n `1076`
- 1h: commodity avg `0.2504` n `13`; crypto_alt avg `-0.6005` n `235`; crypto_major avg `-0.7319` n `8`; equity avg `-0.3529` n `150`; fx avg `-0.0133` n `6`; index avg `-0.0518` n `26`; metal avg `0.0254` n `20`; unknown avg `1.2693` n `1068`
- 4h: commodity avg `0.5365` n `13`; crypto_alt avg `-0.3317` n `235`; crypto_major avg `-0.4222` n `8`; equity avg `0.0164` n `150`; fx avg `-0.0402` n `6`; index avg `-0.0566` n `26`; metal avg `-0.0614` n `20`; unknown avg `5.6112` n `1018`
- 24h: commodity avg `-0.232` n `13`; crypto_alt avg `0.6672` n `235`; crypto_major avg `0.5776` n `8`; equity avg `0.7958` n `149`; fx avg `0.1101` n `6`; index avg `0.1269` n `26`; metal avg `0.0782` n `20`; unknown avg `381.4704` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1694`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
