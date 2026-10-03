# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T08:37:27.136542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `13`; crypto_alt avg `0.009` n `235`; crypto_major avg `-0.0289` n `8`; equity avg `-0.0081` n `143`; fx avg `-0.0022` n `6`; index avg `0.0011` n `26`; metal avg `-0.0093` n `20`; unknown avg `1.0005` n `984`
- 1h: commodity avg `0.0166` n `13`; crypto_alt avg `-0.0736` n `235`; crypto_major avg `-0.0946` n `8`; equity avg `-0.0039` n `143`; fx avg `-0.0026` n `6`; index avg `-0.0023` n `26`; metal avg `-0.0025` n `20`; unknown avg `0.9767` n `966`
- 4h: commodity avg `-0.0092` n `13`; crypto_alt avg `-0.2273` n `235`; crypto_major avg `0.0204` n `8`; equity avg `0.0188` n `143`; fx avg `-0.0032` n `6`; index avg `-0.0035` n `26`; metal avg `0.0074` n `20`; unknown avg `0.0786` n `944`
- 24h: commodity avg `0.6749` n `13`; crypto_alt avg `-2.7248` n `235`; crypto_major avg `-2.6591` n `8`; equity avg `-0.0599` n `142`; fx avg `0.0299` n `6`; index avg `0.1205` n `26`; metal avg `-0.3783` n `20`; unknown avg `-0.4321` n `872`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1814`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
