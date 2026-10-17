# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T05:07:26.488232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `13`; crypto_alt avg `0.1223` n `236`; crypto_major avg `0.1267` n `8`; equity avg `0.0607` n `151`; fx avg `-0.0016` n `6`; index avg `0.0015` n `26`; metal avg `0.0018` n `20`; unknown avg `3.9923` n `1191`
- 1h: commodity avg `-0.0161` n `13`; crypto_alt avg `0.2089` n `236`; crypto_major avg `0.0987` n `8`; equity avg `0.0296` n `151`; fx avg `-0.0026` n `6`; index avg `-0.003` n `26`; metal avg `-0.0104` n `20`; unknown avg `3.901` n `1191`
- 4h: commodity avg `0.0382` n `13`; crypto_alt avg `0.3151` n `236`; crypto_major avg `0.2461` n `8`; equity avg `0.047` n `151`; fx avg `-0.0007` n `6`; index avg `0.0144` n `26`; metal avg `0.019` n `20`; unknown avg `0.3234` n `1183`
- 24h: commodity avg `0.6086` n `13`; crypto_alt avg `-1.3053` n `236`; crypto_major avg `-1.2736` n `8`; equity avg `-4.364` n `151`; fx avg `-0.0335` n `6`; index avg `-0.6975` n `26`; metal avg `-0.2226` n `20`; unknown avg `40.7681` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1739`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1202`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0932`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0768`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
