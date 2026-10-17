# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T01:37:32.277508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.013` n `13`; crypto_alt avg `-0.1929` n `236`; crypto_major avg `-0.0231` n `8`; equity avg `-0.072` n `151`; fx avg `-0.0032` n `6`; index avg `-0.0034` n `26`; metal avg `0.0051` n `20`; unknown avg `0.8986` n `1193`
- 1h: commodity avg `0.0385` n `13`; crypto_alt avg `-0.3122` n `236`; crypto_major avg `-0.2183` n `8`; equity avg `0.0549` n `151`; fx avg `-0.014` n `6`; index avg `-0.0046` n `26`; metal avg `-0.0004` n `20`; unknown avg `1.9528` n `1191`
- 4h: commodity avg `0.0892` n `13`; crypto_alt avg `-0.1758` n `236`; crypto_major avg `-0.2042` n `8`; equity avg `-0.1027` n `151`; fx avg `-0.0008` n `6`; index avg `-0.0262` n `26`; metal avg `-0.0237` n `20`; unknown avg `2.4996` n `1183`
- 24h: commodity avg `0.5386` n `13`; crypto_alt avg `-1.4043` n `236`; crypto_major avg `-1.1408` n `8`; equity avg `-3.8056` n `151`; fx avg `-0.0494` n `6`; index avg `-0.6063` n `26`; metal avg `0.0061` n `20`; unknown avg `41.5555` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1704`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1169`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0926`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0763`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
