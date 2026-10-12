# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T13:52:37.434674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0357` n `13`; crypto_alt avg `0.0339` n `235`; crypto_major avg `0.1278` n `8`; equity avg `-0.1664` n `151`; fx avg `-0.0064` n `6`; index avg `-0.0141` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.9969` n `1134`
- 1h: commodity avg `0.1329` n `13`; crypto_alt avg `-0.3229` n `235`; crypto_major avg `-0.2214` n `8`; equity avg `-0.9398` n `151`; fx avg `0.0021` n `6`; index avg `-0.0627` n `26`; metal avg `-0.0067` n `20`; unknown avg `-0.0448` n `1132`
- 4h: commodity avg `0.3092` n `13`; crypto_alt avg `-1.3722` n `235`; crypto_major avg `-1.0629` n `8`; equity avg `-1.1809` n `151`; fx avg `0.0113` n `6`; index avg `-0.1011` n `26`; metal avg `-0.0635` n `20`; unknown avg `-0.0068` n `1109`
- 24h: commodity avg `0.3138` n `13`; crypto_alt avg `0.2495` n `235`; crypto_major avg `0.1465` n `8`; equity avg `-2.3172` n `151`; fx avg `-0.1026` n `6`; index avg `-0.2375` n `26`; metal avg `-0.0442` n `20`; unknown avg `-0.3769` n `911`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2336`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2055`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
