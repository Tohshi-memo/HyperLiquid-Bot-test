# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T06:07:31.535455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `13`; crypto_alt avg `0.2065` n `235`; crypto_major avg `0.1207` n `8`; equity avg `0.0838` n `150`; fx avg `-0.0115` n `6`; index avg `0.0074` n `26`; metal avg `0.0137` n `20`; unknown avg `-0.0541` n `1046`
- 1h: commodity avg `0.0312` n `13`; crypto_alt avg `0.356` n `235`; crypto_major avg `0.2467` n `8`; equity avg `0.3207` n `150`; fx avg `0.0123` n `6`; index avg `0.0214` n `26`; metal avg `0.0693` n `20`; unknown avg `-0.1613` n `1046`
- 4h: commodity avg `-0.043` n `13`; crypto_alt avg `0.8699` n `235`; crypto_major avg `0.4845` n `8`; equity avg `0.5442` n `150`; fx avg `0.0116` n `6`; index avg `0.0726` n `26`; metal avg `0.1613` n `20`; unknown avg `-0.1808` n `1040`
- 24h: commodity avg `0.0564` n `13`; crypto_alt avg `-1.0298` n `235`; crypto_major avg `-2.0079` n `8`; equity avg `-1.1081` n `150`; fx avg `0.1462` n `6`; index avg `-0.0922` n `26`; metal avg `0.3991` n `20`; unknown avg `5.282` n `985`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
