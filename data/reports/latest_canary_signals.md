# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T05:22:28.102057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `13`; crypto_alt avg `-0.0766` n `236`; crypto_major avg `0.02` n `8`; equity avg `0.0244` n `151`; fx avg `0.0011` n `6`; index avg `0.0127` n `26`; metal avg `-0.0066` n `20`; unknown avg `1.5305` n `1193`
- 1h: commodity avg `-0.0072` n `13`; crypto_alt avg `0.1069` n `236`; crypto_major avg `0.1425` n `8`; equity avg `0.1158` n `151`; fx avg `-0.0005` n `6`; index avg `0.0229` n `26`; metal avg `-0.0123` n `20`; unknown avg `5.3437` n `1191`
- 4h: commodity avg `0.0011` n `13`; crypto_alt avg `0.3209` n `236`; crypto_major avg `0.2941` n `8`; equity avg `0.1034` n `151`; fx avg `0.0003` n `6`; index avg `0.0366` n `26`; metal avg `0.0147` n `20`; unknown avg `1.4288` n `1183`
- 24h: commodity avg `0.5922` n `13`; crypto_alt avg `-1.3947` n `236`; crypto_major avg `-1.1869` n `8`; equity avg `-4.2762` n `151`; fx avg `-0.0068` n `6`; index avg `-0.6762` n `26`; metal avg `-0.2431` n `20`; unknown avg `40.8362` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.175`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0934`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0768`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
