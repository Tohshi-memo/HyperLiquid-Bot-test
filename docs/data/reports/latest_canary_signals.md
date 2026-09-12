# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T12:07:32.355385+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.42` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0043` n `12`; crypto_alt avg `0.0189` n `233`; crypto_major avg `0.0125` n `8`; equity avg `0.0105` n `136`; fx avg `0.0018` n `6`; index avg `0.0027` n `26`; metal avg `-0.0023` n `20`; unknown avg `0.003` n `836`
- 1h: commodity avg `0.0236` n `12`; crypto_alt avg `0.0629` n `233`; crypto_major avg `0.1202` n `8`; equity avg `0.0464` n `136`; fx avg `0.0018` n `6`; index avg `0.0008` n `26`; metal avg `0.0317` n `20`; unknown avg `0.098` n `836`
- 4h: commodity avg `0.0739` n `12`; crypto_alt avg `0.1226` n `233`; crypto_major avg `0.4308` n `8`; equity avg `0.0731` n `136`; fx avg `-0.0026` n `6`; index avg `0.0029` n `26`; metal avg `0.0374` n `20`; unknown avg `0.3776` n `830`
- 24h: commodity avg `-0.0969` n `12`; crypto_alt avg `2.9186` n `233`; crypto_major avg `2.1824` n `8`; equity avg `0.329` n `136`; fx avg `-0.0629` n `6`; index avg `0.1211` n `26`; metal avg `0.0964` n `20`; unknown avg `1.1902` n `692`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
