# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T09:37:28.754632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.59` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0309` n `12`; crypto_alt avg `-0.06` n `233`; crypto_major avg `-0.0114` n `8`; equity avg `-0.0167` n `136`; fx avg `0.0064` n `6`; index avg `-0.0001` n `26`; metal avg `0.0007` n `20`; unknown avg `0.0966` n `838`
- 1h: commodity avg `0.0403` n `12`; crypto_alt avg `-0.0885` n `233`; crypto_major avg `0.0961` n `8`; equity avg `-0.0043` n `136`; fx avg `0.003` n `6`; index avg `-0.0015` n `26`; metal avg `-0.003` n `20`; unknown avg `-0.0577` n `836`
- 4h: commodity avg `0.0414` n `12`; crypto_alt avg `0.372` n `233`; crypto_major avg `0.3803` n `8`; equity avg `-0.0469` n `136`; fx avg `0.0035` n `6`; index avg `0.0077` n `26`; metal avg `0.0037` n `20`; unknown avg `3.4808` n `800`
- 24h: commodity avg `-0.0959` n `12`; crypto_alt avg `1.873` n `233`; crypto_major avg `1.5161` n `8`; equity avg `0.0841` n `136`; fx avg `-0.0634` n `6`; index avg `0.1192` n `26`; metal avg `-0.0063` n `20`; unknown avg `0.9176` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
