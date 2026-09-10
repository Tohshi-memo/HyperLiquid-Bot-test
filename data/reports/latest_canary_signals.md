# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T16:37:34.296665+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.113` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0147` n `12`; crypto_alt avg `-0.0759` n `233`; crypto_major avg `-0.073` n `8`; equity avg `-0.1991` n `135`; fx avg `-0.0002` n `6`; index avg `-0.0082` n `26`; metal avg `-0.0088` n `20`; unknown avg `0.1662` n `790`
- 1h: commodity avg `0.2416` n `12`; crypto_alt avg `-1.0734` n `233`; crypto_major avg `-0.7576` n `8`; equity avg `-0.6784` n `135`; fx avg `0.0315` n `6`; index avg `-0.0868` n `26`; metal avg `-0.1119` n `20`; unknown avg `-0.0623` n `788`
- 4h: commodity avg `0.2849` n `12`; crypto_alt avg `-0.9696` n `233`; crypto_major avg `-1.2009` n `8`; equity avg `-0.0399` n `135`; fx avg `0.0239` n `6`; index avg `-0.0879` n `26`; metal avg `0.0046` n `20`; unknown avg `-0.4833` n `760`
- 24h: commodity avg `0.8122` n `12`; crypto_alt avg `-5.0337` n `233`; crypto_major avg `-4.1271` n `8`; equity avg `-2.1092` n `135`; fx avg `0.1236` n `6`; index avg `-0.2936` n `26`; metal avg `-1.1029` n `20`; unknown avg `-0.7359` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
