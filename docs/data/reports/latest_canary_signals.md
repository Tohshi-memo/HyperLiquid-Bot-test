# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T16:57:00.095643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0725` n `12`; crypto_alt avg `0.5265` n `234`; crypto_major avg `0.502` n `8`; equity avg `0.15` n `140`; fx avg `-0.0221` n `6`; index avg `0.0349` n `26`; metal avg `0.0737` n `20`; unknown avg `1.6285` n `910`
- 1h: commodity avg `0.0519` n `12`; crypto_alt avg `0.207` n `234`; crypto_major avg `-0.0466` n `8`; equity avg `0.149` n `140`; fx avg `-0.016` n `6`; index avg `0.0522` n `26`; metal avg `0.1044` n `20`; unknown avg `0.4329` n `888`
- 4h: commodity avg `0.4885` n `12`; crypto_alt avg `0.5674` n `234`; crypto_major avg `0.3232` n `8`; equity avg `0.8387` n `140`; fx avg `-0.0621` n `6`; index avg `0.122` n `26`; metal avg `0.0038` n `20`; unknown avg `1.675` n `858`
- 24h: commodity avg `0.4301` n `12`; crypto_alt avg `1.356` n `234`; crypto_major avg `1.1283` n `8`; equity avg `0.7371` n `140`; fx avg `-0.2875` n `6`; index avg `0.117` n `26`; metal avg `0.0616` n `20`; unknown avg `0.676` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
