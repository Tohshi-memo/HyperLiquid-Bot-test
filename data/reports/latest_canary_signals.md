# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T13:52:35.160601+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0837` n `13`; crypto_alt avg `0.067` n `235`; crypto_major avg `0.0856` n `8`; equity avg `0.111` n `150`; fx avg `-0.0042` n `6`; index avg `0.0225` n `26`; metal avg `-0.0738` n `20`; unknown avg `17.9863` n `1074`
- 1h: commodity avg `0.2517` n `13`; crypto_alt avg `-0.0009` n `235`; crypto_major avg `0.1335` n `8`; equity avg `0.1812` n `150`; fx avg `-0.027` n `6`; index avg `-0.0146` n `26`; metal avg `-0.0935` n `20`; unknown avg `36.8556` n `1072`
- 4h: commodity avg `0.1412` n `13`; crypto_alt avg `0.3938` n `235`; crypto_major avg `0.5029` n `8`; equity avg `0.5013` n `150`; fx avg `0.0277` n `6`; index avg `0.0683` n `26`; metal avg `-0.0726` n `20`; unknown avg `2.8619` n `1064`
- 24h: commodity avg `-0.3913` n `13`; crypto_alt avg `-0.238` n `235`; crypto_major avg `-0.0758` n `8`; equity avg `1.2163` n `149`; fx avg `0.1026` n `6`; index avg `0.2284` n `26`; metal avg `-0.1033` n `20`; unknown avg `1.3931` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
