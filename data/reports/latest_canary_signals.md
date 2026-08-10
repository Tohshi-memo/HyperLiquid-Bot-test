# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T05:22:31.537062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `0.0028` n `230`; crypto_major avg `0.0172` n `8`; equity avg `0.0152` n `112`; fx avg `-0.0007` n `6`; index avg `0.0134` n `25`; metal avg `-0.0131` n `20`; unknown avg `0.0398` n `785`
- 1h: commodity avg `-0.0534` n `12`; crypto_alt avg `-0.1174` n `230`; crypto_major avg `-0.0264` n `8`; equity avg `-0.056` n `112`; fx avg `0.0289` n `6`; index avg `0.0116` n `25`; metal avg `-0.039` n `20`; unknown avg `0.4869` n `785`
- 4h: commodity avg `-0.068` n `12`; crypto_alt avg `-0.0132` n `230`; crypto_major avg `-0.0147` n `8`; equity avg `-0.2558` n `112`; fx avg `0.0319` n `6`; index avg `0.015` n `25`; metal avg `0.0987` n `20`; unknown avg `1.1839` n `785`
- 24h: commodity avg `0.2945` n `12`; crypto_alt avg `0.692` n `230`; crypto_major avg `-0.0149` n `8`; equity avg `-0.2262` n `112`; fx avg `0.1272` n `6`; index avg `0.0311` n `25`; metal avg `-0.1176` n `20`; unknown avg `-0.3319` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1947`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
