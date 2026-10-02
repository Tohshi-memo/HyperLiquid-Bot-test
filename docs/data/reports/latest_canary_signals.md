# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T02:52:34.635418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0268` n `13`; crypto_alt avg `0.2278` n `234`; crypto_major avg `0.2686` n `8`; equity avg `0.0218` n `142`; fx avg `0.0047` n `6`; index avg `0.0051` n `26`; metal avg `0.053` n `20`; unknown avg `0.0839` n `985`
- 1h: commodity avg `-0.0458` n `13`; crypto_alt avg `0.4431` n `234`; crypto_major avg `0.3983` n `8`; equity avg `0.1248` n `142`; fx avg `-0.0181` n `6`; index avg `0.0208` n `26`; metal avg `0.1623` n `20`; unknown avg `1.8361` n `983`
- 4h: commodity avg `-0.1693` n `13`; crypto_alt avg `1.1221` n `234`; crypto_major avg `0.7629` n `8`; equity avg `0.1471` n `142`; fx avg `-0.0255` n `6`; index avg `0.0516` n `26`; metal avg `-0.0751` n `20`; unknown avg `0.5935` n `977`
- 24h: commodity avg `0.0575` n `13`; crypto_alt avg `0.0959` n `234`; crypto_major avg `0.6446` n `8`; equity avg `0.7434` n `142`; fx avg `-0.2259` n `6`; index avg `0.0877` n `26`; metal avg `-0.0994` n `20`; unknown avg `0.4788` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
