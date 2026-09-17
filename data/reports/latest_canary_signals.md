# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T18:22:31.184333+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0465` n `12`; crypto_alt avg `0.031` n `234`; crypto_major avg `0.0628` n `8`; equity avg `0.0758` n `140`; fx avg `0.0038` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0221` n `20`; unknown avg `-0.3348` n `917`
- 1h: commodity avg `-0.0149` n `12`; crypto_alt avg `-0.0769` n `234`; crypto_major avg `-0.228` n `8`; equity avg `0.0107` n `140`; fx avg `-0.0009` n `6`; index avg `0.0021` n `26`; metal avg `-0.0363` n `20`; unknown avg `0.2877` n `915`
- 4h: commodity avg `0.1587` n `12`; crypto_alt avg `0.3677` n `234`; crypto_major avg `-0.2001` n `8`; equity avg `0.3381` n `140`; fx avg `0.0006` n `6`; index avg `0.0358` n `26`; metal avg `-0.1317` n `20`; unknown avg `1.3199` n `907`
- 24h: commodity avg `0.0273` n `12`; crypto_alt avg `4.5425` n `234`; crypto_major avg `1.9378` n `8`; equity avg `1.8796` n `138`; fx avg `0.0838` n `6`; index avg `0.2803` n `26`; metal avg `0.3459` n `20`; unknown avg `0.2131` n `715`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
