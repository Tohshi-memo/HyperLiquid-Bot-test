# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T11:52:30.158668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `13`; crypto_alt avg `-0.0681` n `237`; crypto_major avg `-0.0986` n `8`; equity avg `-0.0384` n `151`; fx avg `-0.0057` n `6`; index avg `-0.0066` n `26`; metal avg `-0.0091` n `20`; unknown avg `-0.024` n `1193`
- 1h: commodity avg `0.0518` n `13`; crypto_alt avg `-0.1986` n `237`; crypto_major avg `-0.1491` n `8`; equity avg `-0.0676` n `151`; fx avg `0.0072` n `6`; index avg `-0.0139` n `26`; metal avg `-0.0047` n `20`; unknown avg `0.057` n `1191`
- 4h: commodity avg `0.0289` n `13`; crypto_alt avg `0.0044` n `237`; crypto_major avg `0.3525` n `8`; equity avg `0.1632` n `151`; fx avg `-0.0043` n `6`; index avg `0.0247` n `26`; metal avg `0.0201` n `20`; unknown avg `5.0291` n `1079`
- 24h: commodity avg `0.0679` n `13`; crypto_alt avg `-2.4261` n `236`; crypto_major avg `-0.3945` n `8`; equity avg `-0.6759` n `151`; fx avg `-0.0481` n `6`; index avg `-0.0875` n `26`; metal avg `-0.0591` n `20`; unknown avg `4.6257` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2049`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1349`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1305`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.11`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0747`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
