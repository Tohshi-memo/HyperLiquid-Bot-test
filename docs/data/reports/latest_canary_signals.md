# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T04:08:04.978734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0229` n `13`; crypto_alt avg `-0.2506` n `235`; crypto_major avg `-0.1638` n `8`; equity avg `-0.0928` n `144`; fx avg `0.0037` n `6`; index avg `-0.019` n `26`; metal avg `-0.0329` n `20`; unknown avg `0.3543` n `1061`
- 1h: commodity avg `-0.0354` n `13`; crypto_alt avg `-0.6131` n `235`; crypto_major avg `-0.4972` n `8`; equity avg `-0.0278` n `144`; fx avg `0.0017` n `6`; index avg `-0.0127` n `26`; metal avg `0.0402` n `20`; unknown avg `0.7213` n `998`
- 4h: commodity avg `-0.0889` n `13`; crypto_alt avg `-0.2683` n `235`; crypto_major avg `-0.2987` n `8`; equity avg `-0.1116` n `144`; fx avg `-0.1225` n `6`; index avg `-0.0499` n `26`; metal avg `0.0032` n `20`; unknown avg `0.7648` n `986`
- 24h: commodity avg `-0.3242` n `13`; crypto_alt avg `0.6678` n `235`; crypto_major avg `1.0341` n `8`; equity avg `0.2924` n `144`; fx avg `-0.1204` n `6`; index avg `-0.0391` n `26`; metal avg `0.0775` n `20`; unknown avg `0.2992` n `906`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
