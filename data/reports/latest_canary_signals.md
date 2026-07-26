# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T21:22:27.999540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1102` n `12`; crypto_alt avg `0.0709` n `230`; crypto_major avg `0.1457` n `8`; equity avg `0.0369` n `100`; fx avg `0.0086` n `6`; index avg `0.0028` n `25`; metal avg `0.0118` n `20`; unknown avg `-0.0543` n `775`
- 1h: commodity avg `-0.0411` n `12`; crypto_alt avg `0.0279` n `230`; crypto_major avg `0.1315` n `8`; equity avg `0.0718` n `100`; fx avg `-0.0015` n `6`; index avg `-0.0039` n `25`; metal avg `0.0334` n `20`; unknown avg `-0.0601` n `775`
- 4h: commodity avg `0.1351` n `12`; crypto_alt avg `-0.2165` n `230`; crypto_major avg `-0.0799` n `8`; equity avg `0.0051` n `100`; fx avg `0.0367` n `6`; index avg `-0.0377` n `25`; metal avg `0.0467` n `20`; unknown avg `-0.2366` n `775`
- 24h: commodity avg `-0.2777` n `12`; crypto_alt avg `0.9352` n `230`; crypto_major avg `1.0771` n `8`; equity avg `0.6483` n `100`; fx avg `0.0455` n `6`; index avg `0.0972` n `25`; metal avg `0.2229` n `20`; unknown avg `-0.0522` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1912`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
