# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T07:07:36.815107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0393` n `13`; crypto_alt avg `-0.0386` n `234`; crypto_major avg `-0.0068` n `8`; equity avg `0.1284` n `142`; fx avg `-0.0136` n `6`; index avg `0.0315` n `26`; metal avg `0.0033` n `20`; unknown avg `-0.0608` n `983`
- 1h: commodity avg `-0.1346` n `13`; crypto_alt avg `-0.0899` n `234`; crypto_major avg `0.0061` n `8`; equity avg `0.0064` n `142`; fx avg `0.0179` n `6`; index avg `0.012` n `26`; metal avg `-0.1189` n `20`; unknown avg `0.9297` n `981`
- 4h: commodity avg `-0.1492` n `13`; crypto_alt avg `0.7821` n `234`; crypto_major avg `0.9596` n `8`; equity avg `0.0961` n `142`; fx avg `-0.0854` n `6`; index avg `0.0388` n `26`; metal avg `0.0617` n `20`; unknown avg `7.333` n `947`
- 24h: commodity avg `-0.1287` n `13`; crypto_alt avg `-0.0859` n `234`; crypto_major avg `0.9395` n `8`; equity avg `0.2221` n `142`; fx avg `-0.3025` n `6`; index avg `0.0186` n `26`; metal avg `-0.0903` n `20`; unknown avg `1142.2602` n `841`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
