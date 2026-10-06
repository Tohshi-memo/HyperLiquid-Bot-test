# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T04:52:30.429066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0573` n `13`; crypto_alt avg `-0.0285` n `235`; crypto_major avg `-0.0432` n `8`; equity avg `-0.0613` n `149`; fx avg `0.0022` n `6`; index avg `-0.0179` n `26`; metal avg `-0.0404` n `20`; unknown avg `4.7129` n `1072`
- 1h: commodity avg `0.0374` n `13`; crypto_alt avg `0.2794` n `235`; crypto_major avg `0.0861` n `8`; equity avg `-0.0467` n `149`; fx avg `0.028` n `6`; index avg `-0.0123` n `26`; metal avg `-0.0713` n `20`; unknown avg `-0.1369` n `1062`
- 4h: commodity avg `0.1248` n `13`; crypto_alt avg `-0.8903` n `235`; crypto_major avg `-0.5999` n `8`; equity avg `-0.2237` n `149`; fx avg `0.0282` n `6`; index avg `-0.0525` n `26`; metal avg `-0.2148` n `20`; unknown avg `0.144` n `1062`
- 24h: commodity avg `0.0067` n `13`; crypto_alt avg `-0.3084` n `235`; crypto_major avg `0.1215` n `8`; equity avg `0.1388` n `149`; fx avg `0.0438` n `6`; index avg `0.1207` n `26`; metal avg `-0.0087` n `20`; unknown avg `587.401` n `852`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
