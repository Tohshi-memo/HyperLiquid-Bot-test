# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T10:07:26.035707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `13`; crypto_alt avg `-0.1322` n `236`; crypto_major avg `-0.1683` n `8`; equity avg `-0.0204` n `151`; fx avg `0.0114` n `6`; index avg `-0.0068` n `26`; metal avg `-0.0033` n `20`; unknown avg `0.1673` n `1191`
- 1h: commodity avg `0.0209` n `13`; crypto_alt avg `-0.159` n `236`; crypto_major avg `-0.159` n `8`; equity avg `0.0107` n `151`; fx avg `0.0226` n `6`; index avg `0.0225` n `26`; metal avg `-0.0128` n `20`; unknown avg `0.5701` n `1191`
- 4h: commodity avg `-0.1343` n `13`; crypto_alt avg `-0.5206` n `236`; crypto_major avg `-0.0979` n `8`; equity avg `0.0179` n `151`; fx avg `0.0041` n `6`; index avg `0.0147` n `26`; metal avg `0.001` n `20`; unknown avg `0.0046` n `1173`
- 24h: commodity avg `0.3869` n `13`; crypto_alt avg `-1.93` n `236`; crypto_major avg `-1.1374` n `8`; equity avg `-3.5233` n `151`; fx avg `0.0417` n `6`; index avg `-0.5208` n `26`; metal avg `-0.1991` n `20`; unknown avg `8.6345` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1828`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.151`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.125`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1184`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0766`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
