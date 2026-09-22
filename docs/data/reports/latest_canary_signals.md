# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T14:37:36.192425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `12`; crypto_alt avg `-0.9704` n `234`; crypto_major avg `-0.8307` n `8`; equity avg `-0.0498` n `140`; fx avg `-0.0025` n `6`; index avg `-0.005` n `26`; metal avg `-0.015` n `20`; unknown avg `4.1818` n `942`
- 1h: commodity avg `0.2416` n `12`; crypto_alt avg `-0.824` n `234`; crypto_major avg `-0.6019` n `8`; equity avg `0.4286` n `140`; fx avg `-0.0589` n `6`; index avg `0.0704` n `26`; metal avg `-0.0348` n `20`; unknown avg `2.517` n `898`
- 4h: commodity avg `0.4565` n `12`; crypto_alt avg `-0.0842` n `234`; crypto_major avg `-0.081` n `8`; equity avg `0.8187` n `140`; fx avg `-0.0181` n `6`; index avg `0.1334` n `26`; metal avg `0.0978` n `20`; unknown avg `2.0507` n `892`
- 24h: commodity avg `0.0683` n `12`; crypto_alt avg `-0.1624` n `234`; crypto_major avg `0.3818` n `8`; equity avg `1.2851` n `140`; fx avg `-0.2891` n `6`; index avg `0.2514` n `26`; metal avg `0.051` n `20`; unknown avg `8663.5537` n `842`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
