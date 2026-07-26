# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T23:37:08.374379+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0365` n `12`; crypto_alt avg `0.1014` n `230`; crypto_major avg `0.0412` n `8`; equity avg `0.0107` n `100`; fx avg `0.0013` n `6`; index avg `0.0083` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.0328` n `775`
- 1h: commodity avg `0.1038` n `12`; crypto_alt avg `0.0306` n `230`; crypto_major avg `0.0577` n `8`; equity avg `0.0631` n `100`; fx avg `-0.0054` n `6`; index avg `0.0209` n `25`; metal avg `-0.0716` n `20`; unknown avg `-0.1137` n `775`
- 4h: commodity avg `-0.3629` n `12`; crypto_alt avg `0.8863` n `230`; crypto_major avg `1.0768` n `8`; equity avg `0.567` n `100`; fx avg `-0.0044` n `6`; index avg `0.144` n `25`; metal avg `0.1307` n `20`; unknown avg `0.0778` n `775`
- 24h: commodity avg `-0.5125` n `12`; crypto_alt avg `1.7998` n `230`; crypto_major avg `1.9849` n `8`; equity avg `1.1131` n `100`; fx avg `0.0409` n `6`; index avg `0.2363` n `25`; metal avg `0.3569` n `20`; unknown avg `0.1462` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1812`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
