# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T18:37:17.049917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3942` n `12`; crypto_alt avg `-0.0546` n `228`; crypto_major avg `0.0221` n `8`; equity avg `0.0071` n `67`; fx avg `-0.0047` n `6`; index avg `-0.1526` n `23`; metal avg `-0.0077` n `18`; unknown avg `-0.1673` n `405`
- 1h: commodity avg `0.5946` n `12`; crypto_alt avg `-0.115` n `228`; crypto_major avg `0.0283` n `8`; equity avg `0.0194` n `67`; fx avg `0.0143` n `6`; index avg `-0.0122` n `23`; metal avg `-0.045` n `18`; unknown avg `-0.2703` n `405`
- 4h: commodity avg `-0.0961` n `12`; crypto_alt avg `0.375` n `228`; crypto_major avg `-0.345` n `8`; equity avg `0.0627` n `67`; fx avg `-0.005` n `6`; index avg `0.1334` n `23`; metal avg `0.0729` n `18`; unknown avg `-0.1036` n `405`
- 24h: commodity avg `-0.7793` n `12`; crypto_alt avg `2.2328` n `228`; crypto_major avg `0.6327` n `8`; equity avg `0.891` n `67`; fx avg `-0.0166` n `6`; index avg `0.5424` n `23`; metal avg `1.5603` n `18`; unknown avg `1.1977` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
