# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T23:37:32.730782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0234` n `13`; crypto_alt avg `0.0291` n `236`; crypto_major avg `-0.0334` n `8`; equity avg `0.0519` n `151`; fx avg `0.0` n `6`; index avg `0.0022` n `26`; metal avg `-0.0068` n `20`; unknown avg `-0.0271` n `1193`
- 1h: commodity avg `0.0454` n `13`; crypto_alt avg `0.1206` n `236`; crypto_major avg `0.0022` n `8`; equity avg `-0.0849` n `151`; fx avg `0.0097` n `6`; index avg `-0.0137` n `26`; metal avg `-0.0116` n `20`; unknown avg `1.2684` n `1191`
- 4h: commodity avg `0.0381` n `13`; crypto_alt avg `0.8751` n `236`; crypto_major avg `0.8035` n `8`; equity avg `-0.2131` n `151`; fx avg `0.0137` n `6`; index avg `-0.0318` n `26`; metal avg `-0.0172` n `20`; unknown avg `0.8621` n `1107`
- 24h: commodity avg `0.4884` n `13`; crypto_alt avg `-1.0019` n `236`; crypto_major avg `-0.9163` n `8`; equity avg `-3.9167` n `151`; fx avg `0.0416` n `6`; index avg `-0.6183` n `26`; metal avg `-0.0415` n `20`; unknown avg `41.2021` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1667`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1178`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0877`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.077`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0719`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0701`, n `666`, weak_sample_signal
