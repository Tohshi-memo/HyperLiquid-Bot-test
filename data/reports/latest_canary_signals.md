# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T19:52:28.271136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0597` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0201` n `12`; crypto_alt avg `-0.2859` n `230`; crypto_major avg `-0.4052` n `8`; equity avg `-0.345` n `100`; fx avg `-0.0037` n `6`; index avg `-0.0365` n `25`; metal avg `0.0027` n `20`; unknown avg `-0.0833` n `772`
- 1h: commodity avg `-0.1015` n `12`; crypto_alt avg `-0.3178` n `230`; crypto_major avg `-0.4175` n `8`; equity avg `-0.3615` n `100`; fx avg `0.0105` n `6`; index avg `-0.0166` n `25`; metal avg `-0.0012` n `20`; unknown avg `0.0166` n `772`
- 4h: commodity avg `-0.0943` n `12`; crypto_alt avg `-0.8903` n `230`; crypto_major avg `-1.0294` n `8`; equity avg `-0.1707` n `100`; fx avg `0.0225` n `6`; index avg `0.0303` n `25`; metal avg `-0.0512` n `20`; unknown avg `-0.4611` n `772`
- 24h: commodity avg `0.8193` n `12`; crypto_alt avg `-1.6752` n `230`; crypto_major avg `-2.343` n `8`; equity avg `-1.5334` n `99`; fx avg `-0.0661` n `6`; index avg `-0.3481` n `25`; metal avg `-0.7907` n `20`; unknown avg `-0.3532` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
