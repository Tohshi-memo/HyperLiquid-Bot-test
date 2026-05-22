# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T17:22:21.316057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4949` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2684` n `12`; crypto_alt avg `-0.2202` n `228`; crypto_major avg `-0.1498` n `8`; equity avg `-0.1116` n `67`; fx avg `-0.0005` n `6`; index avg `-0.0574` n `23`; metal avg `-0.0869` n `18`; unknown avg `-0.1508` n `386`
- 1h: commodity avg `-0.0039` n `12`; crypto_alt avg `0.0622` n `228`; crypto_major avg `0.0375` n `8`; equity avg `-0.0217` n `67`; fx avg `0.0204` n `6`; index avg `0.0692` n `23`; metal avg `0.0312` n `18`; unknown avg `-0.2559` n `386`
- 4h: commodity avg `-0.1334` n `12`; crypto_alt avg `-1.4067` n `228`; crypto_major avg `-1.2179` n `8`; equity avg `-0.3732` n `67`; fx avg `0.0493` n `6`; index avg `0.277` n `23`; metal avg `-0.3085` n `18`; unknown avg `-0.7913` n `386`
- 24h: commodity avg `-0.8954` n `12`; crypto_alt avg `0.0408` n `228`; crypto_major avg `-1.0085` n `8`; equity avg `-0.0868` n `67`; fx avg `0.1975` n `6`; index avg `0.8782` n `23`; metal avg `-0.8142` n `18`; unknown avg `-1.2594` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0417`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0412`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0409`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0408`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0395`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0388`, n `668`, weak_sample_signal
