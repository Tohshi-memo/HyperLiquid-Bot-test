# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T12:22:25.340622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0709` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1184` n `12`; crypto_alt avg `-1.2385` n `228`; crypto_major avg `-1.1167` n `8`; equity avg `-0.2222` n `74`; fx avg `-0.0013` n `6`; index avg `-0.0509` n `23`; metal avg `-0.0895` n `18`; unknown avg `-0.2195` n `516`
- 1h: commodity avg `0.0961` n `12`; crypto_alt avg `-0.9817` n `228`; crypto_major avg `-1.0016` n `8`; equity avg `-0.1085` n `74`; fx avg `0.0008` n `6`; index avg `0.0693` n `23`; metal avg `-0.0965` n `18`; unknown avg `-0.2881` n `516`
- 4h: commodity avg `0.2879` n `12`; crypto_alt avg `-0.9682` n `228`; crypto_major avg `-1.0014` n `8`; equity avg `-0.1799` n `74`; fx avg `-0.0367` n `6`; index avg `-0.2318` n `23`; metal avg `-0.137` n `18`; unknown avg `-3.9862` n `516`
- 24h: commodity avg `0.1928` n `12`; crypto_alt avg `1.8138` n `228`; crypto_major avg `1.663` n `8`; equity avg `1.5222` n `74`; fx avg `0.0189` n `6`; index avg `0.5638` n `23`; metal avg `0.467` n `18`; unknown avg `-0.1577` n `405`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
