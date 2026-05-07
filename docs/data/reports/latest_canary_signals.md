# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T16:07:20.053924+00:00`
- Correlation status: `ready`
- Asset price records: `564`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6516` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.3561` n `12`; crypto_alt avg `-0.3019` n `228`; crypto_major avg `-0.3049` n `8`; equity avg `-0.659` n `65`; fx avg `0.0121` n `5`; index avg `-0.2945` n `23`; metal avg `-0.3085` n `18`; unknown avg `-0.3957` n `365`
- 1h: commodity avg `0.7971` n `12`; crypto_alt avg `-0.4841` n `228`; crypto_major avg `-0.5456` n `8`; equity avg `-0.944` n `65`; fx avg `0.0548` n `5`; index avg `-0.4932` n `23`; metal avg `-1.0973` n `18`; unknown avg `-0.436` n `365`
- 4h: commodity avg `1.0362` n `12`; crypto_alt avg `-1.3383` n `228`; crypto_major avg `-1.6154` n `8`; equity avg `-1.4037` n `65`; fx avg `0.0542` n `5`; index avg `-0.7255` n `23`; metal avg `-0.9828` n `18`; unknown avg `-0.7373` n `365`
- 24h: commodity avg `-0.1483` n `12`; crypto_alt avg `-0.4453` n `228`; crypto_major avg `-2.4334` n `8`; equity avg `-0.3584` n `65`; fx avg `0.1279` n `5`; index avg `-0.1194` n `23`; metal avg `0.881` n `18`; unknown avg `-0.7854` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1316`, n `560`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1184`, n `560`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1151`, n `560`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1059`, n `560`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0921`, n `556`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0873`, n `556`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0845`, n `556`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `556`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `560`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0724`, n `556`, weak_sample_signal
