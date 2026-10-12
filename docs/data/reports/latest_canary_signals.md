# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T10:07:29.465162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0636` n `13`; crypto_alt avg `-0.087` n `235`; crypto_major avg `-0.0153` n `8`; equity avg `0.0398` n `151`; fx avg `0.008` n `6`; index avg `0.0069` n `26`; metal avg `0.0226` n `20`; unknown avg `0.1887` n `1131`
- 1h: commodity avg `-0.0097` n `13`; crypto_alt avg `-0.3345` n `235`; crypto_major avg `-0.1227` n `8`; equity avg `0.029` n `151`; fx avg `-0.0043` n `6`; index avg `0.0054` n `26`; metal avg `0.0604` n `20`; unknown avg `0.0097` n `1081`
- 4h: commodity avg `0.2496` n `13`; crypto_alt avg `-0.6741` n `235`; crypto_major avg `-0.3845` n `8`; equity avg `-0.4957` n `151`; fx avg `-0.0569` n `6`; index avg `-0.0655` n `26`; metal avg `-0.0128` n `20`; unknown avg `0.3201` n `997`
- 24h: commodity avg `-0.1147` n `13`; crypto_alt avg `1.7803` n `235`; crypto_major avg `1.27` n `8`; equity avg `-1.0379` n `151`; fx avg `-0.1142` n `6`; index avg `-0.1239` n `26`; metal avg `0.0455` n `20`; unknown avg `0.1104` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2146`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
