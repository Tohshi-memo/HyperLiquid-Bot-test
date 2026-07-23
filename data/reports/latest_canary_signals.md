# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T15:37:26.473981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0229` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0208` n `12`; crypto_alt avg `0.1202` n `230`; crypto_major avg `0.1635` n `8`; equity avg `0.2088` n `100`; fx avg `0.0118` n `6`; index avg `0.0166` n `25`; metal avg `0.0334` n `20`; unknown avg `0.0838` n `772`
- 1h: commodity avg `0.1156` n `12`; crypto_alt avg `-0.5994` n `230`; crypto_major avg `-0.6154` n `8`; equity avg `-1.1418` n `100`; fx avg `-0.0075` n `6`; index avg `-0.1874` n `25`; metal avg `-0.1212` n `20`; unknown avg `-0.133` n `772`
- 4h: commodity avg `0.2576` n `12`; crypto_alt avg `-0.7867` n `230`; crypto_major avg `-1.3692` n `8`; equity avg `-1.3513` n `99`; fx avg `0.0046` n `6`; index avg `-0.3463` n `25`; metal avg `-0.3463` n `20`; unknown avg `0.1084` n `772`
- 24h: commodity avg `1.0898` n `12`; crypto_alt avg `-1.4632` n `230`; crypto_major avg `-1.8411` n `8`; equity avg `-2.2093` n `99`; fx avg `-0.0832` n `6`; index avg `-0.4587` n `25`; metal avg `-0.9595` n `20`; unknown avg `-0.2909` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
