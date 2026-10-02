# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T01:52:28.595954+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0225` n `13`; crypto_alt avg `0.3226` n `234`; crypto_major avg `0.2762` n `8`; equity avg `0.1859` n `142`; fx avg `-0.0066` n `6`; index avg `0.0537` n `26`; metal avg `-0.0112` n `20`; unknown avg `1.5268` n `985`
- 1h: commodity avg `-0.0379` n `13`; crypto_alt avg `0.0126` n `234`; crypto_major avg `-0.0413` n `8`; equity avg `-0.1505` n `142`; fx avg `-0.0405` n `6`; index avg `-0.0093` n `26`; metal avg `-0.1452` n `20`; unknown avg `0.576` n `983`
- 4h: commodity avg `-0.1888` n `13`; crypto_alt avg `0.7764` n `234`; crypto_major avg `0.5804` n `8`; equity avg `0.1049` n `142`; fx avg `-0.0115` n `6`; index avg `0.0378` n `26`; metal avg `-0.245` n `20`; unknown avg `0.762` n `961`
- 24h: commodity avg `0.2414` n `13`; crypto_alt avg `-0.0962` n `234`; crypto_major avg `0.1274` n `8`; equity avg `0.8348` n `142`; fx avg `-0.2379` n `6`; index avg `0.1374` n `26`; metal avg `-0.2942` n `20`; unknown avg `0.0171` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
