# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T23:59:11.731257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `13`; crypto_alt avg `0.1531` n `236`; crypto_major avg `0.0211` n `8`; equity avg `0.1341` n `151`; fx avg `-0.0007` n `6`; index avg `0.0083` n `26`; metal avg `0.0033` n `20`; unknown avg `8.6932` n `1193`
- 1h: commodity avg `0.0701` n `13`; crypto_alt avg `0.1713` n `236`; crypto_major avg `-0.0033` n `8`; equity avg `0.0674` n `151`; fx avg `0.0075` n `6`; index avg `-0.0201` n `26`; metal avg `-0.0094` n `20`; unknown avg `5.1061` n `1191`
- 4h: commodity avg `0.074` n `13`; crypto_alt avg `0.7934` n `236`; crypto_major avg `0.5906` n `8`; equity avg `-0.1264` n `151`; fx avg `0.0069` n `6`; index avg `-0.0383` n `26`; metal avg `-0.0022` n `20`; unknown avg `2.4183` n `1107`
- 24h: commodity avg `0.4855` n `13`; crypto_alt avg `-0.9315` n `236`; crypto_major avg `-0.9433` n `8`; equity avg `-3.6042` n `151`; fx avg `0.0382` n `6`; index avg `-0.588` n `26`; metal avg `-0.0212` n `20`; unknown avg `40.6827` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1678`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1179`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1121`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0883`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0771`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0715`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0697`, n `666`, weak_sample_signal
