# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T15:52:20.474676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0291` n `12`; crypto_alt avg `0.0962` n `228`; crypto_major avg `-0.0359` n `8`; equity avg `-0.0413` n `67`; fx avg `-0.0003` n `6`; index avg `0.0246` n `23`; metal avg `0.0307` n `18`; unknown avg `-0.3589` n `396`
- 1h: commodity avg `-0.1736` n `12`; crypto_alt avg `0.2098` n `228`; crypto_major avg `0.0924` n `8`; equity avg `-0.1011` n `67`; fx avg `-0.0047` n `6`; index avg `-0.0931` n `23`; metal avg `0.0739` n `18`; unknown avg `-0.3774` n `396`
- 4h: commodity avg `0.6902` n `12`; crypto_alt avg `-0.8973` n `228`; crypto_major avg `-0.8151` n `8`; equity avg `-0.424` n `67`; fx avg `0.0267` n `6`; index avg `-0.363` n `23`; metal avg `-0.4963` n `18`; unknown avg `0.3685` n `396`
- 24h: commodity avg `-1.4771` n `12`; crypto_alt avg `0.8498` n `228`; crypto_major avg `2.4159` n `8`; equity avg `1.5488` n `67`; fx avg `0.0676` n `6`; index avg `0.5166` n `23`; metal avg `0.6164` n `18`; unknown avg `0.9864` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
