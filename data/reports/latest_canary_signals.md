# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T09:52:26.102756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.59` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0397` n `12`; crypto_alt avg `0.0256` n `233`; crypto_major avg `-0.0138` n `8`; equity avg `-0.0038` n `136`; fx avg `-0.0061` n `6`; index avg `-0.0003` n `26`; metal avg `0.0021` n `20`; unknown avg `0.0131` n `838`
- 1h: commodity avg `0.0828` n `12`; crypto_alt avg `-0.0498` n `233`; crypto_major avg `0.018` n `8`; equity avg `-0.0063` n `136`; fx avg `-0.0051` n `6`; index avg `-0.0036` n `26`; metal avg `-0.0039` n `20`; unknown avg `0.052` n `836`
- 4h: commodity avg `0.0675` n `12`; crypto_alt avg `0.5031` n `233`; crypto_major avg `0.3703` n `8`; equity avg `-0.0343` n `136`; fx avg `-0.0018` n `6`; index avg `0.0005` n `26`; metal avg `0.0111` n `20`; unknown avg `0.1938` n `800`
- 24h: commodity avg `-0.025` n `12`; crypto_alt avg `1.9371` n `233`; crypto_major avg `1.4176` n `8`; equity avg `0.0419` n `136`; fx avg `-0.0547` n `6`; index avg `0.1135` n `26`; metal avg `-0.02` n `20`; unknown avg `0.8551` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
