# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T07:52:28.495719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `-0.0902` n `230`; crypto_major avg `-0.043` n `8`; equity avg `0.0283` n `96`; fx avg `0.0056` n `6`; index avg `0.0016` n `25`; metal avg `-0.0051` n `20`; unknown avg `0.0272` n `770`
- 1h: commodity avg `-0.0181` n `12`; crypto_alt avg `-0.0808` n `230`; crypto_major avg `0.0094` n `8`; equity avg `0.0779` n `96`; fx avg `0.0169` n `6`; index avg `0.0059` n `25`; metal avg `-0.0315` n `20`; unknown avg `-0.0899` n `770`
- 4h: commodity avg `0.0159` n `12`; crypto_alt avg `0.0484` n `230`; crypto_major avg `0.1004` n `8`; equity avg `0.1906` n `96`; fx avg `0.0221` n `6`; index avg `0.0032` n `25`; metal avg `-0.028` n `20`; unknown avg `0.0457` n `752`
- 24h: commodity avg `0.3437` n `12`; crypto_alt avg `0.2771` n `230`; crypto_major avg `0.9584` n `8`; equity avg `0.0996` n `96`; fx avg `0.0041` n `6`; index avg `0.0017` n `25`; metal avg `-0.0533` n `20`; unknown avg `0.0464` n `751`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
