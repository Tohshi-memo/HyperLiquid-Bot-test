# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T12:22:29.800789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.37` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.0115` n `233`; crypto_major avg `-0.0792` n `8`; equity avg `-0.0161` n `136`; fx avg `0.0012` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.1516` n `838`
- 1h: commodity avg `0.0046` n `12`; crypto_alt avg `0.1556` n `233`; crypto_major avg `0.0913` n `8`; equity avg `0.032` n `136`; fx avg `0.0024` n `6`; index avg `-0.0009` n `26`; metal avg `0.0333` n `20`; unknown avg `0.1707` n `836`
- 4h: commodity avg `0.0559` n `12`; crypto_alt avg `0.1017` n `233`; crypto_major avg `0.3408` n `8`; equity avg `0.0607` n `136`; fx avg `-0.0066` n `6`; index avg `0.0049` n `26`; metal avg `0.036` n `20`; unknown avg `0.7291` n `830`
- 24h: commodity avg `-0.0187` n `12`; crypto_alt avg `2.9623` n `233`; crypto_major avg `2.0708` n `8`; equity avg `0.2374` n `136`; fx avg `-0.0517` n `6`; index avg `0.0917` n `26`; metal avg `0.0668` n `20`; unknown avg `1.3301` n `692`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
