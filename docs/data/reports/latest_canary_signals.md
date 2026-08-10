# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T11:37:26.551187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0364` n `12`; crypto_alt avg `0.0558` n `230`; crypto_major avg `0.0359` n `8`; equity avg `0.1372` n `113`; fx avg `0.0048` n `6`; index avg `0.0181` n `25`; metal avg `0.0192` n `20`; unknown avg `-0.0386` n `784`
- 1h: commodity avg `0.0171` n `12`; crypto_alt avg `0.182` n `230`; crypto_major avg `0.1445` n `8`; equity avg `-0.1536` n `113`; fx avg `-0.0001` n `6`; index avg `-0.0247` n `25`; metal avg `-0.0246` n `20`; unknown avg `-0.0842` n `784`
- 4h: commodity avg `0.2378` n `12`; crypto_alt avg `-0.0029` n `230`; crypto_major avg `-0.2412` n `8`; equity avg `-0.3667` n `113`; fx avg `0.0157` n `6`; index avg `-0.0495` n `25`; metal avg `-0.1401` n `20`; unknown avg `0.0328` n `784`
- 24h: commodity avg `0.5613` n `12`; crypto_alt avg `0.9454` n `230`; crypto_major avg `0.0622` n `8`; equity avg `-0.3212` n `113`; fx avg `0.2252` n `6`; index avg `0.0307` n `25`; metal avg `-0.1628` n `20`; unknown avg `57.0296` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
