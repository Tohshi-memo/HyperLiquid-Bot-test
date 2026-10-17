# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T03:52:24.952135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `13`; crypto_alt avg `-0.0868` n `236`; crypto_major avg `0.0051` n `8`; equity avg `-0.0543` n `151`; fx avg `0.0` n `6`; index avg `-0.0016` n `26`; metal avg `0.0046` n `20`; unknown avg `-0.0701` n `1193`
- 1h: commodity avg `0.0117` n `13`; crypto_alt avg `0.3807` n `236`; crypto_major avg `0.2415` n `8`; equity avg `0.0493` n `151`; fx avg `-0.0016` n `6`; index avg `0.0011` n `26`; metal avg `0.0193` n `20`; unknown avg `0.139` n `1191`
- 4h: commodity avg `0.0948` n `13`; crypto_alt avg `-0.0214` n `236`; crypto_major avg `-0.0312` n `8`; equity avg `0.2558` n `151`; fx avg `0.0033` n `6`; index avg `0.0325` n `26`; metal avg `0.0191` n `20`; unknown avg `0.0333` n `1183`
- 24h: commodity avg `0.7069` n `13`; crypto_alt avg `-0.8109` n `236`; crypto_major avg `-0.8515` n `8`; equity avg `-4.1274` n `151`; fx avg `-0.0439` n `6`; index avg `-0.6747` n `26`; metal avg `-0.2504` n `20`; unknown avg `40.5388` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.172`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1185`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1146`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0933`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0763`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0719`, n `666`, weak_sample_signal
