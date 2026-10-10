# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T12:22:26.796101+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0192` n `13`; crypto_alt avg `0.0079` n `235`; crypto_major avg `-0.005` n `8`; equity avg `0.0125` n `150`; fx avg `0.0006` n `6`; index avg `-0.0004` n `26`; metal avg `0.0025` n `20`; unknown avg `0.3279` n `1117`
- 1h: commodity avg `-0.0004` n `13`; crypto_alt avg `0.0672` n `235`; crypto_major avg `0.0633` n `8`; equity avg `0.0257` n `150`; fx avg `0.0014` n `6`; index avg `-0.0017` n `26`; metal avg `0.0018` n `20`; unknown avg `0.5341` n `1109`
- 4h: commodity avg `-0.2323` n `13`; crypto_alt avg `0.0653` n `235`; crypto_major avg `-0.1472` n `8`; equity avg `0.048` n `150`; fx avg `-0.0408` n `6`; index avg `0.0056` n `26`; metal avg `0.0008` n `20`; unknown avg `1.373` n `1109`
- 24h: commodity avg `-0.1514` n `13`; crypto_alt avg `1.5734` n `235`; crypto_major avg `-0.2214` n `8`; equity avg `-0.2448` n `150`; fx avg `0.0267` n `6`; index avg `-0.0268` n `26`; metal avg `0.0465` n `20`; unknown avg `632.2295` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
