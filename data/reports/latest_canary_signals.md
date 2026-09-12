# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T09:22:26.511446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.61` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `-0.0116` n `233`; crypto_major avg `0.0142` n `8`; equity avg `-0.0018` n `136`; fx avg `-0.0054` n `6`; index avg `-0.0039` n `26`; metal avg `-0.0038` n `20`; unknown avg `-0.1022` n `838`
- 1h: commodity avg `0.009` n `12`; crypto_alt avg `-0.1045` n `233`; crypto_major avg `0.1159` n `8`; equity avg `0.0149` n `136`; fx avg `-0.0033` n `6`; index avg `0.0053` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.1537` n `830`
- 4h: commodity avg `-0.0047` n `12`; crypto_alt avg `0.6472` n `233`; crypto_major avg `0.4723` n `8`; equity avg `-0.0444` n `136`; fx avg `-0.0023` n `6`; index avg `0.0082` n `26`; metal avg `0.0025` n `20`; unknown avg `0.1971` n `802`
- 24h: commodity avg `-0.199` n `12`; crypto_alt avg `1.564` n `233`; crypto_major avg `1.1746` n `8`; equity avg `0.0433` n `136`; fx avg `-0.07` n `6`; index avg `0.1181` n `26`; metal avg `-0.0162` n `20`; unknown avg `0.9209` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
