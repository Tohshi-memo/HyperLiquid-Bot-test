# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T23:22:31.710423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `12`; crypto_alt avg `-0.153` n `230`; crypto_major avg `-0.1236` n `8`; equity avg `-0.0437` n `100`; fx avg `0.0018` n `6`; index avg `-0.0128` n `25`; metal avg `-0.0106` n `20`; unknown avg `0.0468` n `775`
- 1h: commodity avg `0.1721` n `12`; crypto_alt avg `0.1157` n `230`; crypto_major avg `0.3099` n `8`; equity avg `0.12` n `100`; fx avg `-0.0068` n `6`; index avg `0.0207` n `25`; metal avg `-0.0392` n `20`; unknown avg `-0.199` n `775`
- 4h: commodity avg `-0.331` n `12`; crypto_alt avg `0.8092` n `230`; crypto_major avg `1.0312` n `8`; equity avg `0.5368` n `100`; fx avg `-0.002` n `6`; index avg `0.1356` n `25`; metal avg `0.1291` n `20`; unknown avg `-0.0522` n `775`
- 24h: commodity avg `-0.481` n `12`; crypto_alt avg `1.7021` n `230`; crypto_major avg `1.9615` n `8`; equity avg `1.1405` n `100`; fx avg `0.0381` n `6`; index avg `0.2282` n `25`; metal avg `0.3546` n `20`; unknown avg `0.1118` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1793`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
