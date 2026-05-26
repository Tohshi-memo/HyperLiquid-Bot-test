# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T00:22:18.913516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.107` n `12`; crypto_alt avg `-0.1613` n `228`; crypto_major avg `-0.2205` n `8`; equity avg `-0.1133` n `67`; fx avg `0.0202` n `6`; index avg `-0.2502` n `23`; metal avg `-0.2237` n `18`; unknown avg `-0.0063` n `407`
- 1h: commodity avg `0.3053` n `12`; crypto_alt avg `-0.2648` n `228`; crypto_major avg `-0.3157` n `8`; equity avg `-0.5351` n `67`; fx avg `-0.0343` n `6`; index avg `-0.2132` n `23`; metal avg `-0.7371` n `18`; unknown avg `-0.199` n `405`
- 4h: commodity avg `0.5526` n `12`; crypto_alt avg `-1.3128` n `228`; crypto_major avg `-0.6768` n `8`; equity avg `-0.8333` n `67`; fx avg `-0.0144` n `6`; index avg `-0.4666` n `23`; metal avg `-0.658` n `18`; unknown avg `-0.5526` n `405`
- 24h: commodity avg `-0.0739` n `12`; crypto_alt avg `0.9069` n `228`; crypto_major avg `-0.4977` n `8`; equity avg `0.014` n `67`; fx avg `0.006` n `6`; index avg `0.1775` n `23`; metal avg `-0.2506` n `18`; unknown avg `0.8059` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1686`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
