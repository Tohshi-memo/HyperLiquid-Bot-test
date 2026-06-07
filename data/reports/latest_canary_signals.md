# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T14:07:22.619572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `72.43` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0474` n `12`; crypto_alt avg `0.046` n `228`; crypto_major avg `0.1599` n `8`; equity avg `0.1059` n `74`; fx avg `-0.0053` n `6`; index avg `0.061` n `23`; metal avg `0.0157` n `18`; unknown avg `0.0131` n `516`
- 1h: commodity avg `-0.1115` n `12`; crypto_alt avg `0.314` n `228`; crypto_major avg `0.3628` n `8`; equity avg `0.3294` n `74`; fx avg `-0.0007` n `6`; index avg `0.1725` n `23`; metal avg `0.0677` n `18`; unknown avg `0.0931` n `516`
- 4h: commodity avg `0.1687` n `12`; crypto_alt avg `-0.5969` n `228`; crypto_major avg `-0.5908` n `8`; equity avg `0.3161` n `74`; fx avg `0.0124` n `6`; index avg `0.2912` n `23`; metal avg `-0.1443` n `18`; unknown avg `0.008` n `516`
- 24h: commodity avg `0.1037` n `12`; crypto_alt avg `1.532` n `228`; crypto_major avg `1.74` n `8`; equity avg `1.64` n `74`; fx avg `0.0244` n `6`; index avg `0.4799` n `23`; metal avg `0.4755` n `18`; unknown avg `-3.7624` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
