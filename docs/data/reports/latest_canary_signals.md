# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T02:07:29.551062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `13`; crypto_alt avg `0.0185` n `235`; crypto_major avg `0.0085` n `8`; equity avg `-0.0005` n `143`; fx avg `-0.0002` n `6`; index avg `0.0027` n `26`; metal avg `-0.0016` n `20`; unknown avg `0.0397` n `1077`
- 1h: commodity avg `0.0258` n `13`; crypto_alt avg `-0.0183` n `235`; crypto_major avg `0.043` n `8`; equity avg `-0.0076` n `143`; fx avg `-0.0014` n `6`; index avg `-0.0023` n `26`; metal avg `0.0005` n `20`; unknown avg `0.3478` n `1077`
- 4h: commodity avg `-0.0538` n `13`; crypto_alt avg `0.154` n `235`; crypto_major avg `0.0469` n `8`; equity avg `0.0097` n `143`; fx avg `-0.0031` n `6`; index avg `-0.0065` n `26`; metal avg `0.0033` n `20`; unknown avg `0.1944` n `1071`
- 24h: commodity avg `0.1695` n `13`; crypto_alt avg `1.4573` n `235`; crypto_major avg `0.6011` n `8`; equity avg `0.1357` n `143`; fx avg `-0.0295` n `6`; index avg `0.0067` n `26`; metal avg `-0.0023` n `20`; unknown avg `-0.0113` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2011`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1866`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
