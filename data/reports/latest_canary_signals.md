# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T06:37:28.336496+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `75.13` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.1065` n `234`; crypto_major avg `-0.0032` n `8`; equity avg `-0.0016` n `140`; fx avg `0.0053` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.1167` n `943`
- 1h: commodity avg `0.0293` n `12`; crypto_alt avg `-0.1477` n `234`; crypto_major avg `0.0537` n `8`; equity avg `-0.0022` n `140`; fx avg `0.0069` n `6`; index avg `0.0001` n `26`; metal avg `0.0106` n `20`; unknown avg `-0.153` n `911`
- 4h: commodity avg `0.0141` n `12`; crypto_alt avg `-1.138` n `234`; crypto_major avg `-0.8497` n `8`; equity avg `-0.4089` n `140`; fx avg `-0.0004` n `6`; index avg `-0.0681` n `26`; metal avg `-0.0149` n `20`; unknown avg `0.8427` n `895`
- 24h: commodity avg `0.2144` n `12`; crypto_alt avg `-0.0962` n `234`; crypto_major avg `-1.8662` n `8`; equity avg `-0.211` n `140`; fx avg `-0.0487` n `6`; index avg `-0.019` n `26`; metal avg `0.0067` n `20`; unknown avg `0.6364` n `816`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
