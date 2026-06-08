# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T06:22:24.928246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1063` n `12`; crypto_alt avg `0.3314` n `228`; crypto_major avg `0.2744` n `8`; equity avg `0.0399` n `74`; fx avg `-0.0274` n `6`; index avg `0.1526` n `23`; metal avg `0.2721` n `18`; unknown avg `0.169` n `517`
- 1h: commodity avg `0.1515` n `12`; crypto_alt avg `0.5515` n `228`; crypto_major avg `0.655` n `8`; equity avg `-0.3577` n `74`; fx avg `-0.079` n `6`; index avg `-0.082` n `23`; metal avg `-0.0669` n `18`; unknown avg `0.0068` n `507`
- 4h: commodity avg `0.2068` n `12`; crypto_alt avg `-0.2737` n `228`; crypto_major avg `-0.2818` n `8`; equity avg `-0.6865` n `74`; fx avg `-0.178` n `6`; index avg `-0.1772` n `23`; metal avg `-0.1189` n `18`; unknown avg `-0.0916` n `507`
- 24h: commodity avg `0.6916` n `12`; crypto_alt avg `0.4199` n `228`; crypto_major avg `2.2797` n `8`; equity avg `0.1587` n `74`; fx avg `-0.2536` n `6`; index avg `-0.0999` n `23`; metal avg `-0.5868` n `18`; unknown avg `-5.5071` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
