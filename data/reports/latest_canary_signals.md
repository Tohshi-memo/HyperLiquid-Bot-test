# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T18:22:35.170549+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0207` n `12`; crypto_alt avg `-0.0507` n `228`; crypto_major avg `0.0025` n `8`; equity avg `-0.1104` n `74`; fx avg `0.0036` n `6`; index avg `-0.0226` n `23`; metal avg `0.2576` n `18`; unknown avg `-0.0354` n `643`
- 1h: commodity avg `-0.0238` n `12`; crypto_alt avg `-0.5214` n `228`; crypto_major avg `-0.2635` n `8`; equity avg `-0.4575` n `74`; fx avg `0.0192` n `6`; index avg `-0.2166` n `23`; metal avg `0.2918` n `18`; unknown avg `-0.1017` n `643`
- 4h: commodity avg `-0.7167` n `12`; crypto_alt avg `-0.2687` n `228`; crypto_major avg `0.549` n `8`; equity avg `-0.0787` n `74`; fx avg `0.0159` n `6`; index avg `0.1232` n `23`; metal avg `1.1334` n `18`; unknown avg `-0.2877` n `643`
- 24h: commodity avg `-0.8136` n `12`; crypto_alt avg `-0.0072` n `228`; crypto_major avg `0.9644` n `8`; equity avg `1.0066` n `74`; fx avg `0.0429` n `6`; index avg `1.1048` n `23`; metal avg `1.6775` n `18`; unknown avg `42.1052` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
